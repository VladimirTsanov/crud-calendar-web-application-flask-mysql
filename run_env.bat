@echo off
cd /d "C:\Users\vtsan\Documents\GitHub\crud-calendar-web-application-flask-mysql"
CALL .envCalendar\Scripts\activate
flask --app server run --debug
pause