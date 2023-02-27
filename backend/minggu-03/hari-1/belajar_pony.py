from pony.orm import *

db = Database()

class Person(db.Entity):
    name = Required(str)
    age = Required(int)
    cars = Set('Car');

class Car(db.Entity):
    make = Required(str)
    model = Required(str)
    owner = Required(Person);

show(Person)

db.bind(provider='postgres', user='postgres', password='postgres', host='localhost', database='db', port='5432')
set_sql_debug(True)
with db_session:
    db.execute("DELETE FROM Person WHERE id > 0")

set_sql_debug(True)
db.generate_mapping(create_tables=True)

#p1 = Person(name='John', age=20)
#commit()
nama = 'john'
umur = 34
with db_session:
    p = Person(name='Kate', age=33)
    p = Person(name='sf', age=20)
    db.execute(f"INSERT INTO Person (name, age) VALUES ('{nama}',{umur})")


