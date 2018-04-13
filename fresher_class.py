class Human(object):
	def __init__(self, name):
		self.name = name
	def walk(self):
		print (self.name + " is walking")
	def get_name(self):
		return (self. name)
	def set_name(self, name):
		if len(name) <= 10:
			self.name = name
human_a = Human("alan")

print (human_a.name)
human_a.set_name('bob')
print(human_a.name)

xy = Human('noah')
print (xy.name)

xy.walk()
xy.set_name('nova')
xy.walk()