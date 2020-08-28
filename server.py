from bottle import run, route, template, redirect, url, static_file, get, post, request
import json
import database as db
from datetime import datetime, date

@route('/')
def home():
    #configs = db.get_all_configs()
    configs = 0
    return template('index.html', configs = configs)    

@post('/save_config')
def save_config():
    print("post called")
#    data = request.json()
    
    config_list = []
    for i in range(0,33):
        config_list.append([i,request.forms.get('ch{}'.format(i))])
    print(config_list)
    print("-------------")
#    print(data)
    print("end of post sending")
    return redirect('/')
@post('/')
def send_config():
    pass
    
@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/')

run(host='0.0.0.0', port=8080, debug=True)
