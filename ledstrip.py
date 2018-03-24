# Import the PCA9685 module.
import Adafruit_PCA9685

class ledstrip():
	pwm = Adafruit_PCA9685.PCA9685()
	
	def red_on(self):
		self.pwm.set_pwm(0, 0, 4095)
		
	def red_off(self):
		self.pwm.set_pwm(0, 0, 0)