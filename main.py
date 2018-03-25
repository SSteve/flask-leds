from flask import Flask, render_template, redirect
from ledstrip import ledstrip

app = Flask(__name__)
leds = ledstrip()

@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/on', methods=['POST'])
def on():
	print('On')
	leds.on()
	return redirect('/')

@app.route('/off', methods=['POST'])
def off():
	leds.off()
	return redirect('/')

@app.route('/setcolor/<color>', methods=['POST'])
def setColor(color):
	leds.set_color(color)
	return redirect('/')

if __name__ == '__main__':
	app.run(host='0.0.0.0')
