class Team:
	
	LEAD = 0
	SKIP = 1
	THIRD = 2
	SECOND = 3
	
	
	
	def __init__(self, lead = None, second = None, third = None, skip = None):
		self.lead = lead
		self.second = second
		self.third = third
		self.skip = skip
		self.player_count = 0
		if (lead is not None):
			self.player_count += 1
		if (second is not None):
			self.player_count += 1
		if(third is not None):
			self.player_count += 1
		if(skip is not None):
			self.player_count += 1
	
	def addPlayer(self, position, name):
		if (position % 4 == LEAD):
			self.lead = name
		elif(position % 4 == SECOND):
			self.second = name
		elif(position % 4 == THIRD):
			self.third == name
		elif(position % 4 == SKIP):
			self.skip == name
		self.player_count += 1
		
	
