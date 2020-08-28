from tinydb import TinyDB, Query

def save_config(config_list, name):
    db = TinyDB('config_db.json')
    res = db.insert({'channels':config_list, 'name':name}, 'current':True)
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

def modify_config():
    pass

def delete_config_by_name(name):
    db = TinyDB('config_db.json')
    query = Query()
    res = db.remove(query.name == name)
    db.close()
    return res
