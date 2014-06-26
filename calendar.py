import datetime


def getTodaysDate():
	todaysDate = datetime.datetime.now()
	return todaysDate
		
def getDateFromOneYearAgo():
	todaysDate = datetime.datetime.now()
	yesterYearsDate = todaysDate.replace(year = todaysDate.year - 1)
	return yesterYearsDate
	
#Returns the day of the week given the date
#0 is Monday, 1 is Tuesday...
def getDayFromDate(date):
	return date.weekday()
	
#Returns the specified date plus one day
def incrementDate(date):
	date += datetime.timedelta(days=1)
	return date
	
	
