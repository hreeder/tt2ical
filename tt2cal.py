#!/usr/bin/env python
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        source = request.form['source']
        soup = BeautifulSoup(source, 'html.parser')

        tables = soup.find_all('table')
        print(len(tables))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5150, debug=True)
