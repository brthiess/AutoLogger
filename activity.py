import score

class Activity:
	
	activityCount = 0
   

	def __init__(self, kind, name,  date, location, venue, duration, supervision, 
	teammates, quality, comment):
		self.kind = kind
		self.name = name	
		self.date = date
		self.location = location
		self.supervision = supervision
		self.duration = duration
		self.quality = quality
		self.comment = comment
		Activity.activityCount += 1
   
	def displayActivityCount(self):
		print "Total Activities %d" % Activity.activityCount 
	
	def to_string(self):
		print ("Kind: " + str(self.kind) + "\tName: " + str(self.name) + "\tDate: " + str(self.date) \
		+ "\tLocation: " + str(self.location) + "\tSupervision: " + str(self.supervision) + \
		"\tDuration: " + str(self.duration) + "\tQuality: " + str(self.quality) + "\tComment: " + str(self.comment) + "\n\n")

