# This is a comment added after the inital commit.

class person():
	def __init__(self, name):
		self.name = name
	def declareCompetency(self):
		print "This is proof that " + self.name + " can commit."

def main():
	dude = person("Benjamin")
	dude.declareCompetency()

main()