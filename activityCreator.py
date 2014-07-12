from activity import Activity
import calendar
import datetime
import quality
import comment
import random
from constants import *





#Get all of the activities for the player and return it as a list
def getActivities(playerName, startDate = None, endDate = None):
	#Check if these parameters were entered
	if (startDate is None):
		startDate = calendar.getDateFromOneYearAgo()
	if (endDate is None):
		endDate = calendar.getTodaysDate()
	
	activities = []
		
	activities.extend(getTactical(playerName, startDate, endDate ))
	activities.extend(getPhysical(playerName, startDate, endDate))
	activities.extend(getTechnical(playerName, startDate, endDate))
	activities.extend(getMental(playerName, startDate, endDate))
	
	return activities
	
#Get all of the tactical activities by the player
#over the specified dates
def getTactical(playerName, startDate, endDate):
	tacticalActivities = []
	activityDate = startDate
	
	numberOfDays = endDate - startDate
	
	#Start from the start date and create all tactical activities
	#within this time period
	for i in range(0, numberOfDays.days):
		#If the date is a Tuesday and it is between September and May
		#then create a tactical activity and add it to the list
		if (calendar.getDayFromDate(activityDate) == TUESDAY and (activityDate.month >= 9 or activityDate.month < 5 )):
			#Get a quality rating
			rating = quality.randomQuality(RANDOM_RATING)
			#Get a comment based off that quality rating
			remark = comment.getComment(TACTICAL, rating)
			#Create the activity and append it to the list
			tacticalActivity = Activity(TACTICAL, playerName, activityDate, SAVILLE, ICE, 
			90, ROB, ALL, rating, remark)
			tacticalActivities.append(tacticalActivity)
		#Increment the date by one day
		activityDate = calendar.incrementDate(activityDate)
	return tacticalActivities
	
def getPhysical(playerName, startDate, endDate):
	physicalActivities = []
	activityDate = startDate
	
	numberOfDays = endDate - startDate
	
	#Start from the start date and create all tactical activities
	#within this time period
	for i in range(0, numberOfDays.days):
		rand = random.randint(1,3)
		#Create workouts on random days (1 out of every 3 on avg)
		#or on the days we workout with a trainer
		if (rand == 3 or calendar.getDayFromDate(activityDate) == THURSDAY):
			#Get a quality rating
			rating = quality.randomQuality(RANDOM_RATING)
			#Get a comment based off that quality rating
			remark = comment.getComment(PHYSICAL, rating)
			time = random.randrange(30,90,15)
			#Create the activity and append it to the list
			if (calendar.getDayFromDate(activityDate) == THURSDAY):
				physicalActivity = Activity(PHYSICAL, playerName, activityDate, SAVILLE, HPTRC, 
				time, ERIC, ALL, rating, remark)
			else:
				physicalActivity = Activity(PHYSICAL, playerName, activityDate, SAVILLE, HPTRC, 
				time, NO_MATES, NO_MATES, rating, remark)
			physicalActivities.append(physicalActivity)
		#Increment the date by one day
		activityDate = calendar.incrementDate(activityDate)
	return physicalActivities
	
def getTechnical(playerName, startDate, endDate):
	technicalActivities = []
	activityDate = startDate
	
	numberOfDays = endDate - startDate
	
	#Start from the start date and create all tactical activities
	#within this time period
	for i in range(0, numberOfDays.days):
		#If it is a Tuesday
		if (calendar.getDayFromDate(activityDate) == TUESDAY and (activityDate.month >= 9 or activityDate.month < 5 )):
			#Get a quality rating
			rating = quality.randomQuality(RANDOM_RATING)
			#Get a comment based off that quality rating
			remark = comment.getComment(TECHNICAL, rating)
			#Create the activity and append it to the list
			technicalActivity = Activity(TECHNICAL, playerName, activityDate, SAVILLE, ICE, 
			60, ROB, ALL, rating, remark)
			technicalActivities.append(technicalActivity)
		#Increment the date by one day
		activityDate = calendar.incrementDate(activityDate)
	return technicalActivities
	
def getMental(playerName, startDate, endDate):
	mentalActivities = []
	activityDate = startDate
	
	numberOfDays = endDate - startDate
	
	#Start from the start date and create all tactical activities
	#within this time period
	for i in range(0, numberOfDays.days):
		rand = random.randint(1,10)
		#Create workouts on random days (1 out of every 10 on avg)
		#or on the days we work with Kyle
		if (rand == 10 or calendar.getDayFromDate(activityDate) == MONDAY):
			#Get a quality rating
			rating = quality.randomQuality(RANDOM_RATING)
			#Get a comment based off that quality rating
			remark = comment.getComment(TECHNICAL, rating)
			time = random.randrange(30,91,15)
			#Create the activity and append it to the list
			mentalActivity = Activity(MENTAL, playerName, activityDate, SAVILLE, ROOM, 
			time, ROB, ALL, rating, remark)
			mentalActivities.append(mentalActivity)
		#Increment the date by one day
		activityDate = calendar.incrementDate(activityDate)
	return mentalActivities
