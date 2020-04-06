from flask import Flask, render_template, redirect, jsonify
from ledstrip import ledstrip

app = Flask(__name__)
leds = ledstrip()

@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/on', methods=['POST', 'GET'])
def on():
	print('On')
	leds.on()
	return jsonify(result="On")

@app.route('/off', methods=['POST', 'GET'])
def off():
	print('Off')
	leds.off()
	return jsonify(result="Off")

@app.route('/setcolor/<color>', methods=['POST', 'GET'])
def setColor(color):
	leds.set_color(color)
	print ("Color: {}".format(color))
	return jsonify(result=color)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
