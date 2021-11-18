from pyPS4Controller.controller import Controller
from motorModule import motor

def limitNumber(num, a, b):
	_num = num
	if (num > b):
		_num = b
	if (num < a):
		_num = a
	return _num

class PS4Controller(Controller):
	def __init__(self, **kwargs):
		Controller.__init__(self, **kwargs)
		self.leftX = 0
		self.leftY = 0

	def on_L3_left(self, value):
		self.leftX = value
		self.update()

	def on_L3_right(self, value):
		self.leftX = value
		self.update()

	def on_L3_up(self, value):
		self.leftY = value * - 1
		self.update()

	def on_L3_down(self, value):
		self.leftY = value * - 1
		self.update()

	def on_L3_x_at_rest(self):
		self.leftX = 0
		self.update()

	def on_L3_y_at_rest(self):
		self.leftY = 0
		self.update()

	def update(self):
		self.mappedX = round(self.leftX / 32767, 4)
		self.mappedY = round(self.leftY / 32767, 4)

		self.leftMotor = self.mappedY
		self.rightMotor = self.mappedY

		if (self.mappedX < 0):
			self.rightMotor += self.mappedX * -1
			self.leftMotor += self.mappedX
		elif (self.mappedX > 0):
			self.rightMotor += self.mappedX * -1
			self.leftMotor += self.mappedX

		self.leftMotor  = limitNumber(self.leftMotor , -1, 1)
		self.rightMotor = limitNumber(self.rightMotor, -1, 1)

		self.leftMotor  = round(self.leftMotor , 2)
		self.rightMotor = round(self.rightMotor, 2)

		if (-0.05 <= self.leftMotor <= 0.05):
			self.leftMotor = 0
		if (-0.05 <= self.rightMotor <= 0.05):
			self.rightMotor = 0


		print(self.leftMotor, self.rightMotor)
		motor.left_motor(self.leftMotor)
		motor.right_motor(self.rightMotor)

controller = PS4Controller(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)