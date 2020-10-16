from tinydb import TinyDB, Query

def save_config(config):
    db = TinyDB('config_db.json')
    for value in config['channels']:
        if value[1] == '':
            value = '0'
        
    res = db.insert({'channels':config['channels'], 'name':config['name'], 'current':"True"})
    db.close()
    return res

def get_config_by_name(name):
    db = TinyDB('config_db.json')
    query = Query()
    res = db.search(query.name == name)
    db.close()
    return res

def get_all_configs():
    db = TinyDB('config_db.json')
    res = db.all()
    db.close()
    return res

def get_current_config():
    db = TinyDB('config_db.json')
    configs = db.all()
    res = {}
    for config in configs:
        if config['current'] == 'True':
            res = config
    db.close()
    return res

def modify_config():
    pass

def delete_config_by_name(name):
    db = TinyDB('config_db.json')
    query = Query()
    res = db.remove(query.name == name)
    db.close()
    return res

def set_all_configs_to_not_current():
    db = TinyDB('config_db.json')
    configs = db.all()
    for config in configs:
        config['current'] = 'False'
    db.close()
