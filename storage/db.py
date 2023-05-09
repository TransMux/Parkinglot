from tinydb import TinyDB, Query



db = TinyDB('车辆信息.json')
User = Query()
db.insert({'name': 'John', 'age': 22})
print(db.search(User.name == 'John'))
