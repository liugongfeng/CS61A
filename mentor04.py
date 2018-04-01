class Baller:

	all_players = []
	def __init__(self, name, has_ball = False):
		self.name = name
		self.has_ball = has_ball
		Baller.all_players.append(self)

	def pass_ball(self, other_player):
		if  self.has_ball:
			self.has_ball = False
			other_player.has_ball = True
			return True
		else:
			return False



class BallHog(Baller):

	def pass_ball(self, other_player):
		return False

"""
>>> ajay = Baller('Ajay', True)
>>> surya = BallHog('Surya')
>>> len(Baller.all_players)
2

>>> Baller.name
Error

>>> len(surya.all_players)
2

>>> ajay.pass_ball()
Error

>>> ajay.pass_ball(surya)
True

>>> ajay.pass_ball(surya)
False

>>> BallHog.pass_ball(surya, ajay)
False

>>> surya.pass_ball(ajay)
False

>>> surya.pass_ball(surya, ajay)
Error

"""




class TeamBaller(Baller):
	"""
	>>> cheerballer = TeamBaller('Thomas', has_ball = True)
	>>> cheerballer.pass_ball(surya)
	Yay!
	True
	>>> cheerballer.pass_ball(surya)
	I don't have the ball
	False
	"""

	def pass_ball(self, other):
		passed = Baller.pass_ball(self, other)
		if passed:
			print('Yay!')
		else:
			print('I don\'t have the ball')
		return passed




class PingPongTracker:
	def __init__(self):
		self.current = 0
		self.index = 1
		self.add = True

	def next(self):
		if self.add:
			self.current += 1
		else:
			self.current -= 1

		if has_seven(self.index) or self.index % 7 == 0:
			self.add = not self.add

		self.index += 1
		return self.current




### Q4

class Bird:

	def __init__(self, call):
		self.call = call
		self.can_fly = True

	def fly(self):
		if self.can_fly:
			return 'Don\'t stop me now!'
		else:
			return 'Ground control to Major Tom...'

	def speak(self):
		print(self.call)




class Chicken(Bird):
	def speak(self, other):
		Bird.speak(self)
		other.speak()


class Penguin(Bird):
	can_fly = False
	def speak(self):
		call = 'Ice to meet you'
		print(call)

