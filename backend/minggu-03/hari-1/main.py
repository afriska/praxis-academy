from flask import Flask, render_template
from pony.flask import Pony
from pony.orm import Required, Database, db_session

app = Flask(__name__)

datasheets = {
    'Nama': 'Arduino Uno',
    'Keterangan': 'Sebuah mikrokontroler',
    'Pin': ['Digital', 'Analog', '5V', '3V', 'GND']
}

Components =["Arduino UNO", "Wemos", "Servo", "ESP8266", 
           "Relay", "LCD", "LED", 'Arduino Mega','Stepper']

@app.route('/')
def home ():
    return render_template('index.html')

@app.route('/datasheet')
def link():
    return render_template('datasheet.html', 
                           data = datasheets,
                           len = len(Components), 
                           Components = Components)


ds = Database()
class Component(ds.Entity):
    nama = Required(str)
    #keterangan = Required(str)
    pinout = set('pin')

class Pin(ds.Entity):
    digital = Required(bool)
    analog = Required(bool)
    v5 = Required(bool)
    v33 = Required(bool)
    GND = Required(bool)


ds.bind(provider='postgres', user='postgres', password='postgres', database='ds', host='localhost')

with db_session:
    ds.execute(f"DELETE FROM Component WHERE id > 0")
ds.generate_mapping(create_tables='TRUE')
with db_session:
    for i in Components:
        ds.execute(f"INSERT INTO Component(nama) VALUES ('{i}')")
#--------------------------------------------------------------------------------------------------------------------------------#
