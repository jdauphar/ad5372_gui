from bottle import run, route, template, redirect, url, static_file, get, post
import json
from datetime import datetime, date

@route('/',)
def home():
    return template('index.html')    

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')

run(host='0.0.0.0', port=8080, debug=True)
