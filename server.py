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
    config = {'config_list':[], 'name':""}
    for i in range(0,33):
        config['config_list'].append([i,request.forms.get('ch{}'.format(i))])
    config['name'] = request.forms.get('config_name_to_save')
    db.save_config(config['config_list'], config['name'])



@post('/')
def send_config():
    pass
    
@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/')

run(host='0.0.0.0', port=8080, debug=True)
