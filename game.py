import score

class Game:
	
	gameCount = 0
   

	def __init__(self, name, date, event, location, opponent, score, supervision,
	technicalRating, tacticalRating, physicalRating, mentalRating,
	overallRating, comment):
		self.name = name
		self.date = date
		self.event = event
		self.location = location
		self.opponent = opponent
		self.score = score
		self.supervision = supervision
		self.technicalRating = technicalRating
		self.tacticalRating = tacticalRating
		self.physicalRating = physicalRating
		self.mentalRating = mentalRating
		self.overallRating = overallRating
		self.comment = comment
		Game.gameCount += 1
   
	def displayGameCount(self):
		print "Total Games %d" % Game.gameCount

