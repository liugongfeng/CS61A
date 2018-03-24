### Question 1.1
"""Below we have defined the classes Instructor, Student, and TeachingAssistant,
implementing some of what was described above. Remember that we pass the self
argument implicitly to instance methods when using dot-notation. """

class Instructor:
	degree = 'PhD (Magic)'   		# This is a class attribute

	def __init__(self, name):
		self.name = name 		# this is an instance attribute

	def lecture(self, topic):
		print('Today we\'re learning about ' + topic)


dumbledore = Instructor('Dumbledore')
class Student:
	instructor = dumbledore

	def __init__(self, name, ta):
		self.name = name
		self.understanding = 0
		ta.add_student(self)

	def attend_lecture(self, topic):
		Student.instructor.lecture(topic)
		if Student.instructor == dumbledore:
			print(Student.instructor.name + ' is awesome!')
		else:
			print('I miss Dumbledore.')
		self.understanding += 1

	def visit_office_hours(self, staff):
		staff.assist(self)
		print('Thanks, ' + staff.name)



class TeachingAssistant:
	def __init__(self, name):
		self.name = name
		self.students = {}

	def add_student(self, student):
		self.students[student.name] = student

	def assist(self, student):
		student.understanding += 1






# -------------------------------------------------------------------

### Question 1.2
"""We now want to write three different classes, Mailman, Client, and Email to simulate
email. Fill in the definitions below to finish the implementation! """

class  Email:
	"""Every email object has 3 instance attributes: 
	the message, the sender name, and the recipient name."""
	def __init__(self, msg, sender_name, recipient_name):
		self.msg = msg
		self.sender_name = sender_name
		self.recipient_name = recipient_name



class Mailman:
	"""Each Mailman has an instance attribute clients, which 
	is a dictionary that associates client names with client objects"""
	def __init__(self):
		self.clients = {}

	def send(self, email):
		"""Take an email and put it in the inbox of the client
		it is addressed to"""
		client = self.clients[email.recipient_name]
		client.receive(email)

	def register_client(self, client, client_name):
		"""Takes a client object and client_name and adds it 
		to the clients instance attribute. """
		self.clients[client_name] = client



class Client:
	"""Every Client has instance attributes name (which is
used for addressing emails to the client), mailman
(which is used to send emails out to other clients), and
inbox (a list of all emails the client has received). """
	def __init__(self, mailman , name):
		self.inbox = []
		self.mailman = mailman
		self.name = name
		self.mailman.register_client(self, self.name)

	def compose(self, msg, recipient_name):
		"""Send an email with the given message msg to the 
		given recipient client. """
		email = Email(msg, self.name, recipient_name)
		self.mailman.send(email)

	def receive(self, email):
		"""Take an email and add it to the inbox of this 
		client. """
		self.inbox.append(email)







# ------------------------------------------------------

#############
#Inheritance#
#############

class Pet(object):
	def __init__(self, name, owner):
		self.is_alive = True 		# It's alive!!
		self.name = name
		self.owner = owner

	def eat(self, thing):
		print(self.name + 'ate a ' + str(thing) + '!')

	def talk(self):
		print(self.name)


class Dog(Pet):
	def __init__(self, name, owner):
		Pet.__init__(name, owner)

	def talk(self):
		print(self.name + ' says woof!')



# Question 2.1

""" Implement the Cat class by inheriting from the Pet class. Make sure to use superclass
methods wherever possible. In addition, add a lose_life method to the Cat class. """

class Cat(Pet):
	def __init__(self, name, owner, lives = 9):
		Pet.__init__(name, owner)
		self.lives = lives

	def talk(self):
		""" A cat says meow! when asked to talk"""
		print(self.name + ' says meow!')

	def lose_life(self):
		"""A cat can only lose a life if they have at least
		one life. when lives reaches zero. 'is_alive' becomes False"""
		if self.lives>0:
			self.lives -= 1
		elif self.lives == 0:
			self.is_alive = False
		else:
			print('This cat has no more lives to lose :(')

### Question 2.2

"""More cats! Fill in the methods for NoisyCat, which is just like a normal Cat.
However, NoisyCat talks a lot, printing twice whatever a Cat says. """

class NoisyCat(Cat):

	"""A Cat that repeats things twice."""
	# def __init__(self, name, owner, lives = 9):

	def talk(self):
		"""Repeat what a Cat says twice."""
		Cat.talk(self)
		Cat.talk(self)





### Question 2.3

class A:
	def f(self):
		return 2

	def g(self, obj, x):
		if x == 0:
			return A.f(obj)
		return obj.f() + self.g(self, x - 1)


class B(A):
	def f(self):
		return 4





### Question 2.4
"""Implement the Yolo class so that the following interpreter session works as expected.

>>> x = Yolo(1)
>>> x.g(3)
4
>>> x.g(5)
6
>>> x.motto = 5
>>> x.g(5)
10
"""

class Yolo:
	def __init__(self, motto):
		self.motto = motto

	def g(self, num):
		return num + self.motto





