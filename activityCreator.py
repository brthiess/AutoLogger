import activity
import calendar
import datetime
import quality
import comment
from constants import *



#Get all of the activities for the player and return it as a list
def getActivities(playerName, startDate = None, endDate = None):
	#Check if these parameters were entered
	if (startDate is None):
		startDate = calendar.getDateFromOneYearAgo()
	if (endDate is None):
		endDate = calendar.getTodaysDate()
		
	getTactical(playerName, startDate, endDate )
	getPhysical(playerName, startDate, endDate)
	getTechnical(playerName, startDate, endDate)
	getMental(playerName, startDate, endDate)
	
#Get all of the tactical activities by the player
#over the specified dates
def getTactical(playerName, startDate, endDate):
	#Start from the start date and create all tactical activities
	#within this time period
	print startDate
	print endDate
	activityDate = startDate
	print startDate.day
	print endDate.day
	numberOfDays = endDate - startDate
	for i in range(0, numberOfDays.days):
		print i
		#If the date is a Tuesday and it is between September and May
		#then create a tactical activity and add it to the list
		if (calendar.getDayFromDate(activityDate) == TUESDAY and (activityDate.month >= 9 or activityDate.month < 5 )):
			#Get a quality rating
			print activityDate
			quality = quality.randomQuality()
			#Get a comment based off that quality rating
			comment = comment.getComment(TACTICAL, quality)
			tacticalActivity = Activity(TACTICAL, playerName, activityDate, SAVILLE, ICE, 
			90, ROB, ALL, quality, comment)
		activityDate = activityDate.replace(day = activityDate.day + 1)
	
def getPhysical(playerName, startDate, endDate):
	return 0
	
def getTechnical(playerName, startDate, endDate):
	return 0
	
def getMental(playerName, startDate, endDate):
	return 0
