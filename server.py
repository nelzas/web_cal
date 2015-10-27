import os
import pathlib
import calendar

from bottle import route, run, static_file, template, redirect

PORT = int(os.environ.get("PORT", 5000))
BASE_PATH = pathlib.Path(__file__).parent


@route('/')
def home():
    return 'Hello world! ' + calendar.HTMLCalendar().formatmonth(2015, 10)


@route('/test_tpl')
@route('/test_tpl/<name>')
def test_tpl(name='World'):
    return template('tpl_test', name=name, next_year=2011) + calendar.HTMLCalendar().formatyear(theyear=2010)


@route('/<display_year:int>/')
def the_year(display_year):
    return template('tpl_year', prev_year=display_year-1, next_year=display_year+1) + \
        calendar.HTMLCalendar().formatyear(theyear=display_year)


@route('/<display_year:int>/<display_month:int>/')
def the_month(display_year, display_month):
    prev_month=display_month-1
    next_month=display_month+1
    year_for_prev_month = display_year
    year_for_next_month = display_year
    if prev_month == 0:
        prev_month = 12
        year_for_prev_month -= 1
    if next_month == 13:
        next_month = 1
        year_for_next_month += 1
    return template('tpl_month',
                    year_for_prev_month=year_for_prev_month,
                    prev_month=prev_month,
                    year_for_next_month=year_for_next_month,
                    next_month=next_month) + \
        calendar.HTMLCalendar().formatmonth(theyear=display_year,
                                            themonth=display_month)


@route('<path:re:.+[^/]$>')
def add_slash(path):
    return redirect(path + "/")


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=str(BASE_PATH / 'static'))


run(host='0.0.0.0', port=PORT)
