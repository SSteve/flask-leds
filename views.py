from flask import render_template, request, redirect
from main import app, leds

@app.route('/')
def homepage():
	return render_template('homepage.html')
	
@app.route('/on', methods=['POST'])
def on():
	leds.red_on()
	return redirect('/')

@app.route('/off', methods=['POST'])
def off():
	leds.red_off()
	return redirect('/')