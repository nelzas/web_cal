import os
import pathlib
import calendar

from bottle import route, run, static_file

PORT = int(os.environ.get("PORT", 5000))
BASE_PATH = pathlib.Path(__file__).parent


@route('/')
def home():
    return 'Hello world! ' + calendar.HTMLCalendar().formatmonth(2015, 10)


@route('/<display_year:int>/')
def the_year(display_year):
    return calendar.HTMLCalendar().formatyear(theyear=display_year)


@route('/<display_year:int>/<display_month:int>/')
def the_month(display_year, display_month):
    return calendar.HTMLCalendar().formatmonth(theyear=display_year,
                                               themonth=display_month)


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=str(BASE_PATH / 'static'))


run(host='0.0.0.0', port=PORT)
