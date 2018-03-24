from flask import Flask
from ledstrip import ledstrip
import views

app = Flask(__name__)
leds = ledstrip()

if __name__ == '__main__':
	app.run(host='0.0.0.0')
	
