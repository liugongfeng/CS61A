"""to evaluate expressions that contain the + operator,
Python checks for special methods on both the left and right operands of the expression.
First, Python checks for an __add__ method on the value of the left operand,
then checks for an __radd__ method on the value of the right operand.
If either is found, that method is invoked with the value of the other operand as its argument.
"""

class Number:
	def __add__(self, other):
		return self.add(other)

	def __mul__(self, other):
		return self.mul(other)



class Complex(Number):
	def add(self, other):
		return ComplexRI(self.real + other.real, self.imag + other.imag)

	def mul(self, other):
		magnitude = self.magnitude * other.magnitude
		return ComplexMA(magnitude, self.angle + other.angle)



from math import atan2
class ComplexRI(Complex):
	def __init__(self, real, imag):
		self.real = real
		self.imag = imag

	@property
	def magnitude(self):
		return (self.real ** 2 + self.imag ** 2) ** 0.5


	@property
	def angle(self):
		return atan2(self.imag, self.real)

	def __repr__(self):
		return 'ComplexRI({0:g}, {1:g})'.format(self.real, self.imag)
"""
>>> ri = ComplexRI(5, 12)
>>> ri.real
5
>>> ri.magnitude
13.0
>>> ri.real = 9
>>> ri.real
9
>>> ri.magnitude 
15.0
"""

from math import sin, cos, pi
class ComplexMA(Complex):

	def __init__(self, magnitude, angle):
		self.magnitude = magnitude
		self.angle = angle

	@property
	def real(self):
		return self.magnitude * cos(self.angle)


	@property
	def imag(self):
		return self.magnitude * sin(self.angle)

	def __repr__(self):	
		return 'ComplexMA({0:g}, {1:g}*pi)'.format(self.magnitude, self.angle/pi)

"""
>>> ma = ComplexMA(2, pi/2)
>>> ma.imag
2.0
>>> ma.angle = pi
>>> ma.real
-2.0

>>> from math import pi
>>> ComplexRI(1, 2) + ComplexMA(2, pi/2)
ComplexRI(1, 4)
>>> ComplexRI(0, 1) * ComplexRI(0, 1)
ComplexMA(1, 1*pi)

"""


