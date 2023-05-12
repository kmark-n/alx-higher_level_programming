Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from
Example of a parent class;

class Person(object):
	#constructor
	def __init__(self, name, id):
		self.name = name
		self.id = id
	#To check if this person is an employee
	def Display(self):
		print(self.name, self.id)
#Drive code
emp = Person("Mark", 260) #An object of a person
emp = Display ()
