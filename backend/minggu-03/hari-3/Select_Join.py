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

#show(Person)

db.bind(provider='postgres', user='postgres', password='postgres', host='localhost', database='db', port='5432')
db.generate_mapping(create_tables=True)
# print('end')
# with db_session:
#     db.execute("DELETE FROM Person WHERE id > 0")

# # set_sql_debug(True)


# #p1 = Person(name='John', age=20)
# #commit()
# nama = 'john'
# umur = 34
# with db_session:
#     p = Person(name='Kate', age=33)
#     p = Person(name='sf', age=20)
#     db.execute(f"INSERT INTO Person (name, age) VALUES ('{nama}',{umur})")

# print('start testing')
# with db_session:
#     orang = select(i for i in Person).order_by(Person.name)[:]
#     print(type(orang))
#     for indiv in orang:
#         print (f'{indiv.name}')

# with db_session:
#     orang = db.execute('SELECT * FROM Person')
#     print(orang, type(orang))
#     names = []
#     for i in orang:
#         print(i, type(i))
#         names.append(f'{i[1]}')
        
    
#     print(names, type(names))

# with db_session:
#     db.execute("UPDATE Person SET name = 'hanan' WHERE name = 'sf'") 
# with db_session:
#     jane = Person.get(name="john")
#     print(jane, type(jane))
#     jane.name = 'Jane'
#     commit()

#-----------------------------------------------------------------------#

with db_session:
    punyaHonda = select(p for p in Person
                          for c in p.cars
                          if 'Honda' in c.make)
    # print(punyaHonda, type(punyaHonda))
    
    for i in punyaHonda:
         lst_model=[]
         for car in i.cars:
             print(f'{i.name} punya mobil model {car.model}') 
             
             

         

# with db_session:
#     mobilnyaKevin = select(c for c in Car #att car
#                              for p in c.owner 
#                              if p.name == 'kevin')
#     for i in mobilnyaKevin:
#         print(f'{i.owner.name} punya mobil {i.model} buatan {i.make} dengan personID {i.owner.id}.')
   
# with db_session:
#     mobilnyaKevin = select(p for p in Person
#                              for c in p.cars
#                              if p.name == 'kevin')
#     for i in mobilnyaKevin:
#         print(f"{i.cars.make.key}")