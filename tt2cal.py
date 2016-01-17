#!/usr/bin/env python
import cStringIO
import datetime
import htmlmin
import icalendar
import os
import zipfile

from bs4 import BeautifulSoup
from flask import Flask, render_template, request, send_file, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(2048)


def get_calendars(source):
    source = htmlmin.minify(source, remove_empty_space=True, remove_comments=True)
    soup = BeautifulSoup(source, 'html.parser')

    header_tables = soup.find_all('table', class_="header-border-args")
    body_tables = soup.find_all('table', class_="grid-border-args")

    # Merge the headers and bodies together
    timetables = zip(header_tables, body_tables)
    calendars = []

    for header, body in timetables:
        ical = icalendar.Calendar()
        ical.add('version', '2.0')

        title = header.find(class_='header-0-0-0').text
        week1 = None
        header_1_2_1 = header.find(class_='header-1-2-1').text
        if header_1_2_1 == "1" or header_1_2_1.startswith("1-"):
          week1 = header.find(class_='header-1-2-3').text.split("-")[0]
        else:
          print("Cannot find the start date of week 1")
          raise Exception

        week1 = datetime.datetime.strptime(week1, '%d %b %Y')
        ical.add('dtstart', week1)

        # First row is the timeslot indicator
        day_rows = body.contents[1:]

        daynum = 0
        for day in day_rows:
            time = 9
            # First col is the day indicator
            events = day.contents[1:]
            for event in events:
                # Blank spaces are \xa0 (non blanking space)
                if event.text == u"\xa0":
                    time += 1
                else:
                    evt = icalendar.Event()
                    hours = int(event['colspan'])

                    info = event.find_all('td')

                    code = info[0].text
                    staff = info[1].text.split(";")
                    module = info[2].text
                    event_type = info[3].text
                    room = info[4].text
                    weeks = info[6].text

                    excludes = None
                    last_week = 0

                    if ", " in weeks:
                        multi_weeks = weeks.split(", ")
                        first_week = 1
                        covered = set()
                        all = set()
                        for weekset in multi_weeks:
                            f = int(weekset.split("-")[0])
                            l = int(weekset.split("-")[1])
                            if f < first_week:
                                first_week = f
                            if l > last_week:
                                last_week = l
                            covered = covered.union(set(xrange(f, l+1)))

                        all = set(xrange(first_week, last_week+1))
                        excludes = all.difference(covered)
                        # print excludes
                    else:
                        last_week = int(weeks.split("-")[-1])

                    # print code, staff, module, event_type, room, weeks, hours
                    start = week1 + datetime.timedelta(days=daynum, hours=time)
                    evt.add('dtstart', start)
                    evt.add('dtend', start+datetime.timedelta(hours=hours))
                    evt.add('summary', module + " " + event_type)
                    evt.add('location', room)
                    evt.add('description', "Module: %s\nStaff: %s\n" % (module, ", ".join(staff)))
                    evt.add('rrule', {
                        'freq': ['WEEKLY'],
                        'count': last_week
                    })

                    if excludes:
                        excludes = [start + datetime.timedelta(weeks=exweek) for exweek in excludes]
                        evt.add('exdate', excludes)

                    ical.add_component(evt)
                    time += hours
            daynum += 1
        calendars.append(ical)
    return calendars


def cal_to_file(calendar):
    output = cStringIO.StringIO()
    output.write(calendar.to_ical())
    output.seek(0)
    return output


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        source = request.form['source']
        if not source:
            flash("You didn't enter anything!")
            return render_template('index.html')
        try:
            calendars = get_calendars(source)
            output = None
            filename = None
            if len(calendars) > 1:
                files = [cal_to_file(cal) for cal in calendars]
                n = 1
                output = cStringIO.StringIO()
                with zipfile.ZipFile(output, 'w') as zf:
                    for file in files:
                        name = "calendar_" + str(n) + ".ics"
                        n+=1
                        zf.writestr(name, file.getvalue())
                output.seek(0)
                filename = "calendars.zip"
            else:
                # Create a file from the single calendar
                output = cal_to_file(calendars[0])
                filename = "calendar.ics"

            return send_file(output, attachment_filename=filename, as_attachment=True)
        except Exception:
            flash("Parsing failed, please try again.")
            return render_template("index.html")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5150, debug=True)
