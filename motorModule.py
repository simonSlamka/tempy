import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class motor():
	def __init__(self,EnaA,In1A,In2A,EnaB,In1B,In2B):
		self.EnaA = EnaA
		self.In1A = In1A
		self.In2A = In2A
		self.EnaB = EnaB
		self.In1B = In1B
		self.In2B = In2B
		GPIO.setup(self.EnaA,GPIO.OUT)
		GPIO.setup(self.In1A,GPIO.OUT)
		GPIO.setup(self.In2A,GPIO.OUT)
		GPIO.setup(self.EnaB,GPIO.OUT)
		GPIO.setup(self.In1B,GPIO.OUT)
		GPIO.setup(self.In2B,GPIO.OUT)
		self.pwmA = GPIO.PWM(self.EnaA, 100);
		self.pwmA.start(0);
		self.pwmB = GPIO.PWM(self.EnaB, 100);
		self.pwmB.start(0);

		# Defining left motor speed
	def left_motor(self,leftspeed=0.5, t=0):
		leftspeed *= 100
		# if function that makes sure we cant exeed a value that we cannot pass to PWM
		if leftspeed > 100:
			leftspeed = 100
		elif leftspeed < -100:
			leftspeed = -100

		# The abs function removes the minus sign if there is any, as we cannot pass a negativ number to PWM
		self.pwmA.ChangeDutyCycle(abs(leftspeed))

		if leftspeed > 0:
			print(f'Left: {leftspeed}')
			GPIO.output(self.In1A,GPIO.HIGH)
			GPIO.output(self.In2A,GPIO.LOW)
		elif leftspeed < 0:
			print(f'Left: {leftspeed}')
			GPIO.output(self.In1A,GPIO.LOW)
			GPIO.output(self.In2A,GPIO.HIGH)

		sleep(t)

	# Defining right motor speed
	def right_motor(self, rightspeed=0.5, t=0):
		rightspeed *= 100
		# if function that makes sure we cant exeed a value that we cannot pass to PWM

		if rightspeed > 100:
			rightspeed = 100
		elif rightspeed < -100:
			rightspeed = -100


		# The abs function removes the minus sign if there is any, as we cannot pass a negativ number to PWM
		self.pwmB.ChangeDutyCycle(abs(rightspeed))
		# this if statement reverses the polarity of the motors if the value is negative

		if rightspeed > 0:
			print(f'Right: {rightspeed}')
			GPIO.output(self.In1B,GPIO.HIGH)
			GPIO.output(self.In2B,GPIO.LOW)
		elif rightspeed < 0:
			print(f'Right: {rightspeed}')
			GPIO.output(self.In1B,GPIO.LOW)
			GPIO.output(self.In2B,GPIO.HIGH)

		sleep(t)

	def stop(self):
		GPIO.output(self.EnaA, GPIO.LOW)
		GPIO.output(self.In1A, GPIO.LOW)
		GPIO.output(self.In2A, GPIO.LOW)
		GPIO.output(self.EnaB, GPIO.LOW)
		GPIO.output(self.In1B, GPIO.LOW)
		GPIO.output(self.In2B, GPIO.LOW)


motor = motor(2, 3, 4, 22, 17, 27)


def main():
	motor.right_motor(50, 2)
	motor.stop()
	motor.left_motor(50, 2)
	motor.stop()

if __name__ == '__main__':
	print('Motortest')
	motor = motor(2, 3, 4, 22, 17, 27)
	main()
	print('Test complete!')
