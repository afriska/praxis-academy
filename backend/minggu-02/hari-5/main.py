from flask import Flask, render_template

app = Flask(__name__)

datasheets = {
    'Nama': 'Arduino Uno',
    'Keterangan': 'Sebuah mikrokontroler',
    'Pin': ['Digital', 'Analog', '5V', '3V', 'GND']
}

Components =["Arduino Mega", "Wemos", "Servo", "ESP8266", 
           "Relay", "LCD", "LED"]

@app.route('/')
def home ():
    return render_template('index.html')

@app.route('/datasheet')
def link():
    return render_template('datasheet.html', 
                           data = datasheets,
                           len = len(Components), 
                           Components = Components)


