def live(lon):
	def prosper(spock, live):
		nonlocal lon
		if len(lon) == 1:
			return spock + 1
		lon[1] = live(lon[0])
		lon = lon[1:]
		prosper(lon[0], abs)
		return spock[0] + 1
	prosper(lon, lambda trek: trek - 3)




class Worker:
	greeting = 'Sir'
	def __init__(self):
		self.elf = Worker

	def work(self):
		return self.greeting + ', I work'

	def __repr__(self):
		return Bourgeoisie.greeting


class Bourgeoisie(Worker):
	greeting = 'Peon'
	def work(self):
		print(Worker.work(self))
		return 'My job is to gather wealth'


class Proletariat(Worker):
	greeting = 'Comrade'
	def work(self, other):
		other.greeting = self.greeting + ' ' + other.greeting
		other.work()
		return other




"""
Implement the look method of the Dress
class. The look method returns a Dress instance’s current color when the number
of times that the instance’s look method has ever been invoked evenly divides the
total number times that the look method of any Dress instance has ever been invoked.
Otherwise, the instance’s color changes to the most recently returned color
from any call to look, and None is returned."""

class Dress:
	"""What color is the dress?
	>>> blue = Dress('blue')
	>>> blue.look()
	'blue'
	>>> gold = Dress('gold')
	>>> gold.look()
	'gold'
	>>> blue.look() # 2 does not evenly divide 3; changes to gold
	>>> Dress('black').look()
	'black'
	>>> gold.look() # 2 does not evenly divide 5; changes to black
	>>> gold.look() # 3 evenly divides 6
	'black'
	>>> Dress('white').look()
	'white'
	>>> gold.look() # 4 evenly divides 8
	'black'
	>>> blue.look() # 3 evenly divides 9
	'gold'
	"""
	seen = 0
	color = None

	def __init__(self, color):
		self.color = color
		self.seen = 0

	def look(self):
		Dress.seen += 1
		self.seen += 1

		if Dress.seen % self.seen == 0:
			Dress.color = self.color
			return self.color
		else:
			self.color = Dress.color


