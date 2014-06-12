class Score:   

	def __init__(self, totalEnds, ourScores, theirScores):
		self.totalEnds = totalEnds		
		self.ourScores = ourScores
		self.theirScores = theirScores

			
	def getOurScoreInEnd(self, end):
		return ourScores[end]
		
		
	def getTheirScoreInEnd(self, end):
		return theirScores[end]
