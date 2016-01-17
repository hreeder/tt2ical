import htmlmin

from bs4 import BeautifulSoup

source = u"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns='http://www.w3.org/1999/xhtml'>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>SWSCUST Object Individual</title>
<link href="swscustom.css" rel="stylesheet" type="text/css" />
</head>

<body>

<!-- START REPORT HEADER -->
<table class='header-border-args'  border='0' cellspacing='0' width='100%'><tr>
<td>
<table cellspacing='0' border='0' width='100%' class='header-0-args'>
<col align='left' /><col align='center' /><col align='right' />
  <tr>
    <td><span class='header-0-0-0'>Merch.B56.co</span><span class='header-0-0-1'> - </span><span class='header-0-0-2'>Computing - Games Lab</span></td><td></td><td></td>
  </tr>
</table>
</td>
</tr><tr>
<td>
<table cellspacing='0' border='0' width='100%' class='header-1-args'>
<col align='left' /><col align='center' /><col align='right' />
  <tr>
    <td></td><td></td><td><span class='header-1-2-0'><a href='default.aspx?context=teachingweeks' target='_blank'>Weeks</a>: </span><span class='header-1-2-1'>1</span><span class='header-1-2-2'> (</span><span class='header-1-2-3'>11 Jan 2016-17 Jan 2016</span><span class='header-1-2-4'>)</span></td>
  </tr>
</table>
</td>
</tr>
</table>
<!-- END REPORT HEADER -->

<table class='grid-border-args' cellspacing='0'  >

<!-- START COLUMN LABELS ONE -->
<tr>
    <td></td>
    
    <td   class='col-label-one' colspan='1'>9:00</td>
    <td   class='col-label-one' colspan='1'>10:00</td>
    <td   class='col-label-one' colspan='1'>11:00</td>
    <td   class='col-label-one' colspan='1'>12:00</td>
    <td   class='col-label-one' colspan='1'>13:00</td>
    <td   class='col-label-one' colspan='1'>14:00</td>
    <td   class='col-label-one' colspan='1'>15:00</td>
    <td   class='col-label-one' colspan='1'>16:00</td>
    <td   class='col-label-one' colspan='1'>17:00</td>
</tr>

<!-- END COLUMN LABELS ONE -->

<!-- START ROW OUTPUT -->
<tr >
    <td style=";" rowspan='1' class='row-label-one'>Mon</td>
    <td style=";" class='cell-border'>&nbsp;</td>
    <td style=";" style='' class='Practical' colspan='2' rowspan='1' >
<!-- START OBJECT-CELL -->
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-0-0' />
  <col class='object-cell-0-2' />
<tr>
  <td align='left'>SET07109.P1a</td>
  <td align='right'>Dr Kevin Chalmers;Dr Simon Powers;Dr Neil Urquhart</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-1-0' />
  <col class='object-cell-1-2' />
<tr>
  <td align='left'>Programming Fundamentals</td>
  <td align='right'>Practical</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-2-0' />
  <col class='object-cell-2-1' />
  <col class='object-cell-2-2' />
<tr>
  <td align='left'>Merch.B56.co</td>
  <td align='center'></td>
  <td align='right'>1-10,  13-15</td>
</tr>
</table>
<!-- END OBJECT-CELL -->
    </td>
    <td style=";" class='cell-border'>&nbsp;</td>
    <td style=";" style='' class='Practical' colspan='4' rowspan='1' >
<!-- START OBJECT-CELL -->
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-0-0' />
  <col class='object-cell-0-2' />
<tr>
  <td align='left'>SET10110.P1</td>
  <td align='right'>Dr Ben Kenwright</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-1-0' />
  <col class='object-cell-1-2' />
<tr>
  <td align='left'>Advanced Game Engineering</td>
  <td align='right'>Practical</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-2-0' />
  <col class='object-cell-2-1' />
  <col class='object-cell-2-2' />
<tr>
  <td align='left'>Merch.B56.co</td>
  <td align='center'></td>
  <td align='right'>1-10,  13-15</td>
</tr>
</table>
<!-- END OBJECT-CELL -->
    </td>
    <td style=";" class='cell-border'>&nbsp;</td>
</tr>
<tr >
    <td style=";" rowspan='1' class='row-label-one'>Tue</td>
    <td style=";" class='cell-border'>&nbsp;</td>
    <td style=";" style='' class='Practical' colspan='2' rowspan='1' >
<!-- START OBJECT-CELL -->
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-0-0' />
  <col class='object-cell-0-2' />
<tr>
  <td align='left'>SET07109.P1e</td>
  <td align='right'>Dr Kevin Chalmers;Dr Simon Powers;Dr Neil Urquhart</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-1-0' />
  <col class='object-cell-1-2' />
<tr>
  <td align='left'>Programming Fundamentals</td>
  <td align='right'>Practical</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-2-0' />
  <col class='object-cell-2-1' />
  <col class='object-cell-2-2' />
<tr>
  <td align='left'>Merch.B56.co</td>
  <td align='center'></td>
  <td align='right'>1-10,  13-15</td>
</tr>
</table>
<!-- END OBJECT-CELL -->
    </td>
    <td style=";" class='cell-border'>&nbsp;</td>
    <td style=";" style='' class='Practical' colspan='2' rowspan='1' >
<!-- START OBJECT-CELL -->
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-0-0' />
  <col class='object-cell-0-2' />
<tr>
  <td align='left'>SET09109.P1a</td>
  <td align='right'>Prof Jon Kerridge</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-1-0' />
  <col class='object-cell-1-2' />
<tr>
  <td align='left'>Fundamentals of Parallel Systems</td>
  <td align='right'>Practical</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-2-0' />
  <col class='object-cell-2-1' />
  <col class='object-cell-2-2' />
<tr>
  <td align='left'>Merch.B56.co</td>
  <td align='center'></td>
  <td align='right'>1-10,  13-15</td>
</tr>
</table>
<!-- END OBJECT-CELL -->
    </td>
    <td style=";" style='' class='Practical' colspan='2' rowspan='1' >
<!-- START OBJECT-CELL -->
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-0-0' />
  <col class='object-cell-0-2' />
<tr>
  <td align='left'>SET07109.P1c</td>
  <td align='right'>Dr Kevin Chalmers;Dr Simon Powers;Dr Neil Urquhart</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-1-0' />
  <col class='object-cell-1-2' />
<tr>
  <td align='left'>Programming Fundamentals</td>
  <td align='right'>Practical</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-2-0' />
  <col class='object-cell-2-1' />
  <col class='object-cell-2-2' />
<tr>
  <td align='left'>Merch.B56.co</td>
  <td align='center'></td>
  <td align='right'>1-10,  13-15</td>
</tr>
</table>
<!-- END OBJECT-CELL -->
    </td>
    <td style=";" class='cell-border'>&nbsp;</td>
</tr>
<tr >
    <td style=";" rowspan='1' class='row-label-one'>Wed</td>
    <td style=";" class='cell-border'>&nbsp;</td>
    <td style=";" class='cell-border'>&nbsp;</td>
    <td style=";" style='' class='Practical' colspan='2' rowspan='1' >
<!-- START OBJECT-CELL -->
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-0-0' />
  <col class='object-cell-0-2' />
<tr>
  <td align='left'>SET08116.P1b</td>
  <td align='right'>Dr Ben Kenwright</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-1-0' />
  <col class='object-cell-1-2' />
<tr>
  <td align='left'>Computer Graphics</td>
  <td align='right'>Practical</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-2-0' />
  <col class='object-cell-2-1' />
  <col class='object-cell-2-2' />
<tr>
  <td align='left'>Merch.B56.co</td>
  <td align='center'></td>
  <td align='right'>1-10,  13-15</td>
</tr>
</table>
<!-- END OBJECT-CELL -->
    </td>
    <td style=";" class='cell-border'>&nbsp;</td>
    <td style=";" class='cell-border'>&nbsp;</td>
    <td style=";" class='cell-border'>&nbsp;</td>
    <td style=";" class='cell-border'>&nbsp;</td>
    <td style=";" class='cell-border'>&nbsp;</td>
</tr>
<tr >
    <td style=";" rowspan='1' class='row-label-one'>Thu</td>
    <td style=";" style='' class='Practical' colspan='2' rowspan='1' >
<!-- START OBJECT-CELL -->
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-0-0' />
  <col class='object-cell-0-2' />
<tr>
  <td align='left'>SET07109.P1d</td>
  <td align='right'>Dr Kevin Chalmers;Dr Simon Powers;Dr Neil Urquhart</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-1-0' />
  <col class='object-cell-1-2' />
<tr>
  <td align='left'>Programming Fundamentals</td>
  <td align='right'>Practical</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-2-0' />
  <col class='object-cell-2-1' />
  <col class='object-cell-2-2' />
<tr>
  <td align='left'>Merch.B56.co</td>
  <td align='center'></td>
  <td align='right'>1-10,  13-15</td>
</tr>
</table>
<!-- END OBJECT-CELL -->
    </td>
    <td style=";" class='cell-border'>&nbsp;</td>
    <td style=";" style='' class='Practical' colspan='2' rowspan='1' >
<!-- START OBJECT-CELL -->
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-0-0' />
  <col class='object-cell-0-2' />
<tr>
  <td align='left'>SET08116.P1a</td>
  <td align='right'>Dr Ben Kenwright</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-1-0' />
  <col class='object-cell-1-2' />
<tr>
  <td align='left'>Computer Graphics</td>
  <td align='right'>Practical</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-2-0' />
  <col class='object-cell-2-1' />
  <col class='object-cell-2-2' />
<tr>
  <td align='left'>Merch.B56.co</td>
  <td align='center'></td>
  <td align='right'>1-10,  13-15</td>
</tr>
</table>
<!-- END OBJECT-CELL -->
    </td>
    <td style=";" style='' class='Practical' colspan='2' rowspan='1' >
<!-- START OBJECT-CELL -->
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-0-0' />
  <col class='object-cell-0-2' />
<tr>
  <td align='left'>SET09109.P1b</td>
  <td align='right'>Prof Jon Kerridge</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-1-0' />
  <col class='object-cell-1-2' />
<tr>
  <td align='left'>Fundamentals of Parallel Systems</td>
  <td align='right'>Practical</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-2-0' />
  <col class='object-cell-2-1' />
  <col class='object-cell-2-2' />
<tr>
  <td align='left'>Merch.B56.co</td>
  <td align='center'></td>
  <td align='right'>1-10,  13-15</td>
</tr>
</table>
<!-- END OBJECT-CELL -->
    </td>
    <td style=";" class='cell-border'>&nbsp;</td>
    <td style=";" class='cell-border'>&nbsp;</td>
</tr>
<tr >
    <td  rowspan='1' class='row-label-one'>Fri</td>
    <td  class='cell-border'>&nbsp;</td>
    <td  style='' class='Practical' colspan='2' rowspan='1' >
<!-- START OBJECT-CELL -->
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-0-0' />
  <col class='object-cell-0-2' />
<tr>
  <td align='left'>SET07109.P1b</td>
  <td align='right'>Dr Kevin Chalmers;Dr Simon Powers;Dr Neil Urquhart</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-1-0' />
  <col class='object-cell-1-2' />
<tr>
  <td align='left'>Programming Fundamentals</td>
  <td align='right'>Practical</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-2-0' />
  <col class='object-cell-2-1' />
  <col class='object-cell-2-2' />
<tr>
  <td align='left'>Merch.B56.co</td>
  <td align='center'></td>
  <td align='right'>1-10,  13-15</td>
</tr>
</table>
<!-- END OBJECT-CELL -->
    </td>
    <td  class='cell-border'>&nbsp;</td>
    <td  style='' class='Practical' colspan='2' rowspan='1' >
<!-- START OBJECT-CELL -->
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-0-0' />
  <col class='object-cell-0-2' />
<tr>
  <td align='left'>SET08116.P1c</td>
  <td align='right'>Dr Ben Kenwright</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-1-0' />
  <col class='object-cell-1-2' />
<tr>
  <td align='left'>Computer Graphics</td>
  <td align='right'>Practical</td>
</tr>
</table>
<table class='object-cell-args' cellspacing='0' border='0' width='100%'>
  <col class='object-cell-2-0' />
  <col class='object-cell-2-1' />
  <col class='object-cell-2-2' />
<tr>
  <td align='left'>Merch.B56.co</td>
  <td align='center'></td>
  <td align='right'>1-10,  13-15</td>
</tr>
</table>
<!-- END OBJECT-CELL -->
    </td>
    <td  class='cell-border'>&nbsp;</td>
    <td  class='cell-border'>&nbsp;</td>
    <td  class='cell-border'>&nbsp;</td>
</table>

<!-- START REPORT FOOTER --><br/>
<!-- This file can contain items to go at the bottom of the Timetable Reports 

This example contains the last week,  print next week links -->

<form name="form1" method="post" action="ShowTimetable.aspx" id="form1">
  <div>
    <input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
    <input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
  </div>
</form>

<script type="text/javascript">
  <!--
var theForm = document.forms['form1'];
if (!theForm) {
    theForm = document.form1;
}
function __doPostBack(eventTarget,  eventArgument) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
}
// -->
</script>

<table border='0' width='100%'>
  <tr>
    <td align='left' width='33%'>
      <font face='arial' size='1'>
        <a id="bLastWeek" href="javascript:__doPostBack('bLastWeek',  '');">Previous Week</a>
      </font>
    </td>
    <td align='center' width='33%'>
      <font face='arial' size='1'>
        <a id="bPrint" href="javascript:__doPostBack('bPrint',  '');"><a href='javascript:window.print();'>Print Timetable</a></a>
      </font>
    </td>
    <td align='right' width='33%'>
      <font face='arial' size='1'>
        <a id="bNextWeek" href="javascript:__doPostBack('bNextWeek',  '');">Next Week</a>
      </font>
    </td>
  </tr>
</table>

<table border='0' width='100%'>
  <tr>
    <td align='left' width='50%'>
      <font face='arial' size='1'>
        <a id="bNextWeek" href="javascript:__doPostBack('bSelection',  '');">Back To Selection</a>
      </font>
    </td>
    <td align='right' width='50%'>
      <font face='arial' size='1'>
        <script language="JavaScript" type="text/JavaScript">document.write(Date())</script>
      </font>
    </td>
    
  </tr>
</table>
<br/>
<hr />
<font size='1' face='arial'> <a href='key.htm' target='_blank'>Key to Activity Type Colours</a></body>
</html>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">"""
source = htmlmin.minify(source, remove_empty_space=True, remove_comments=True)
soup = BeautifulSoup(source, 'html.parser')

header_tables = soup.find_all('table', class_="header-border-args")
body_tables = soup.find_all('table', class_="grid-border-args")

# Merge the headers and bodies together
timetables = zip(header_tables, body_tables)

for timetable in timetables:
    header = timetable[0]
    body = timetable[1]

    title = header.find(class_='header-0-0-0').text

    # First row is the timeslot indicator
    day_rows = body.contents[1:]

    for day in day_rows:
        time = 9
        # First col is the day indicator
        events = day.contents[1:]
        for event in events:
            # Blank spaces are \xa0
            if event.text == u"\xa0":
                time += 1
            else:
                hours = int(event['colspan'])
                time += hours

                info = event.find_all('td')

                code = info[0].text
                staff = info[1].text.split(";")
                module = info[2].text
                event_type = info[3].text
                room = info[4].text
                weeks = info[6].text

                print code, staff, module, event_type, room, weeks, hours
