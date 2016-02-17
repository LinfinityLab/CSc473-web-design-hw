# views.py
from coreapp import app
from flask import url_for, request
import datetime

@app.route('/')
def index():
    page = """
    	<DOCTYPE! html>
    	<html lang="en-US">
    	<head>
    	<title>Day of the Week</title>
    	<meta charset=utf-8">
    	</head>
    	<body>
    	<h1>Enter a date</h1>
    	<p> Enter a date below and submit and we will find the day of the week.</p>
    	<form action = "/dow" method="get">

        <select name="day">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
            <option value="7">7</option>
            <option value="8">8</option>
            <option value="9">9</option>
            <option value="10">10</option>
            <option value="11">11</option>
            <option value="12">12</option>
            <option value="13">13</option>
            <option value="14">14</option>
            <option value="15">15</option>
            <option value="16">16</option>
            <option value="17">17</option>
            <option value="18">18</option>
            <option value="19">19</option>
            <option value="20">20</option>
            <option value="21">21</option>
            <option value="22">22</option>
            <option value="23">23</option>
            <option value="24">24</option>
            <option value="25">25</option>
            <option value="26">26</option>
            <option value="27">27</option>
            <option value="28">28</option>
            <option value="29">29</option>
            <option value="30">30</option>
            <option value="31">31</option>
        </select>

        <select name="month">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
            <option value="7">7</option>
            <option value="8">8</option>
            <option value="9">9</option>
            <option value="10">10</option>
            <option value="11">11</option>
            <option value="12">12</option>
        </select>

        <select name= "year">
            <option value="2014">2014</option>
            <option value="2015">2015</option>
            <option value="2016">2016</option>
            <option value="2017">2017</option>
            <option value="2018">2018</option>
            <option value="2019">2019</option>
            <option value="2020">2020</option>
        </select>

        <input type="submit" value="submit">
        </form>
    	</body>
    	</html>
    	"""
    
    return page

def weekofday(y,m,d):
    """
    The weekday function takes as input three strings that are 
    day month and year to then return the day of the week corresponding
    to those inputs.
    """
    try:
       l = datetime.date(int(y),int(m),int(d))    
    except Exception as e:
       error_msg(e)

    d = {0 :"Monday",
         1 :"Tuesday",
         2 :"Wednesday",
         3 :"Thursday",
         4 :"Friday",
         5 :"Saturday",
         6 :"Sunday"
        }
    return d[l.weekday()]


@app.route('/dow')
def dayofweek():
    page="""
    <DOCTYPE! html>
    <html lang='en-US'>
    <head>
    <meta charset="utf-8">
    <title>Day of the week?</title>
    </head>
    <body>
    <h1>Day of the Week</h1>
    <p>{0}</p>
    </body>
    </html>
    """
    if (len(request.args.keys())==3):
        day = request.args["day"]
        month = request.args["month"]
        year  = request.args["year"]
        daystring = weekofday(year,month,day)    

        return page.format(daystring)
    else:
        return page.format("Error: Missing, incomplete, or incorrect input.<br>400: Bad Request")