from bottle import run, route, template, redirect, url, static_file, get, post, request
import json
import database as db
from datetime import datetime, date

@route('/')
def home():
    saved_configs = db.get_all_configs()
    current_config = db.get_current_config()
    return template('index.html', saved_configs = saved_configs, current_config = current_config)    

@post('/save_config')
def save_config():
    db.set_all_configs_to_not_current()
    print("post called")
    config = {'channels':[], 'name':""}
    for i in range(0,32):
        config['channels'].append([i,request.forms.get('ch{}'.format(i))])
    config['name'] = request.forms.get('config_name_to_save')
    db.save_config(config)
    print(config)
    return redirect('/')


@post('/')
def send_config():
    pass
    
@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/')

run(host='0.0.0.0', port=8080, debug=True)
