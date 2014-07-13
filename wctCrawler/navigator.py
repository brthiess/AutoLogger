import datetime


#Is given the html for a page, and decides which URL to visit next
EVENT = "Arial,Helvetica,Geneva"
EVENTLINK = "A HREF="
SCORES = ">Scores</a></td>"
HTTPWORLDCURL = "http://www.worldcurl.com/"
EVENTSURL = "http://www.worldcurl.com/schedule.php?eventtypeid=21&eventyear=2013"
LINESCORE = "linescoredrawlink"
DRAWLINK = "showdrawid"
VIEWPREVIOUSSEASON = 'View Previous Season'

MEN_2012 = 'http://www.worldcurl.com/schedule.php?eventtypeid=21&eventyear=2012'
MEN_2013 = 'http://www.worldcurl.com/schedule.php?eventtypeid=21&eventyear=2013'
MEN_2014 = 'http://www.worldcurl.com/schedule.php?eventtypeid=21&eventyear=2014'
MEN_2015 = 'http://www.worldcurl.com/schedule.php?eventtypeid=21'
WOMEN_2012 = 'http://www.worldcurl.com/schedule.php?eventtypeid=51&eventyear=2012'
WOMEN_2013 = 'http://www.worldcurl.com/schedule.php?eventtypeid=51&eventyear=2013'
WOMEN_2014 = 'http://www.worldcurl.com/schedule.php?eventtypeid=51&eventyear=2014'
WOMEN_2015 = 'http://www.worldcurl.com/schedule.php?eventtypeid=51'
visitedUrls = []

#Figure out the next page to visit
#latest_update_date: 	The latest date of the games recorded in the games.dat file.  Don't bother
#					visiting events that have already been recorded in the file  
def getNextPage(html, web_url):
	#Figure out the latest date in the games file.  (No use checking for games that have already been recorded)
	latest_update_date = getLatestUpdateDate()
	#Go through the HTML line by line, check for relevant links
	for line in html:
		#Check for events first.  Check to make sure event is not older than the latest date (i.e. already in games.dat)
		if (EVENT in line and EVENTLINK in line and eventIsNotOlderThanLatestDate(web_url, html, line, latest_update_date)):
			#Grab the event URL
			url = line.split("<A HREF=")
			url = url[1].split(">")
			if (hasNotBeenVisitedYet(url[0])):
				visitedUrls.append(url[0])
				return HTTPWORLDCURL + url[0]
		#Check for the scores link next
		elif (SCORES in line):
			url = line.split("href=")
			url = url[1].split(">")
			if (hasNotBeenVisitedYet(url[0])):
				visitedUrls.append(url[0])
				return HTTPWORLDCURL + url[0]
		#Finally, check for the link so specific draws
		elif (LINESCORE in line):
			url = line.replace("href='", " ").replace("'>", " ").split()
			for u in url:
				if (DRAWLINK in u and hasNotBeenVisitedYet(u)):
					visitedUrls.append(u)
					return HTTPWORLDCURL + u
					
	#If nothing found, go back to beginning of page or new schedule page
	return getCorrectSchedulePage(html, web_url)


#Checks to see if a url has been visited by the crawler already
def hasNotBeenVisitedYet(url):
	if url in visitedUrls:
		return False
	else:
		return True
		
#Checks to see if every event for every year for both genders has been visited
def getCorrectSchedulePage(html, web_url):
		
		#If we have hit the end of a schedules page
		#Append that url to the list and find a new schedule page
		#Else do not append the schedule url to the visited urls
		for h in html:
			if (VIEWPREVIOUSSEASON in h):	
				visitedUrls.append(web_url)
		if (hasNotBeenVisitedYet(MEN_2012)):
			return MEN_2012
		elif(hasNotBeenVisitedYet(MEN_2013)):
			return MEN_2013
		elif(hasNotBeenVisitedYet(MEN_2014)):
			return MEN_2014
		elif(hasNotBeenVisitedYet(WOMEN_2012)):
			return WOMEN_2012
		elif(hasNotBeenVisitedYet(WOMEN_2013)):
			return WOMEN_2013
		elif(hasNotBeenVisitedYet(WOMEN_2014)):
			return WOMEN_2014
		else:
			return None

#Checks if the current event being looked at has a date that 
#is older than the latest date in the games.dat file
def eventIsNotOlderThanLatestDate(web_url, html, line, latest_update_date):
	for h in range(0, len(html)):
		if (line in html[h]):
			event_date = getDate(web_url, html[h+4])
			#If the event happened after the latest event in the data file 
			#then we can look at this event for linescores.  
			#Else return false so we don't bother looking for it
			if (event_date > latest_update_date):
				return True
			else:
				return False
	
#Is given the line of html that contains the event date 
#and parses it out and returns it	
def getDate(web_url, html_line):
	#Returns the year the event is played in
	year = getYear(web_url, html_line)
	month = 0
	day = 0
	#Check which month is indicated on the line
	if ('Jan' in html_line):
		#Somewhat obtuse lines of code here...
		#Grabs the day number (1 - 31), from finding the index of substring of the month			Add 4 to get the end of the weekend.  (It's too complex to get end date from html.  It is easier just to get beginning date and then add a few days.  This assumption might break for a slam though.  I'd like to fix this eventually)
		day = html_line[html_line.index('Jan') + 4:-len(html_line) + html_line.index('Jan') + 4 + 2] + str(4)
		month = 1
	elif ('Feb' in html_line):
		day = html_line[html_line.index('Feb') + 4:-len(html_line) + html_line.index('Feb') + 4 + 2] + str(4)
		month = 2
	elif ('Mar' in html_line):
		day = html_line[html_line.index('Mar') + 4:-len(html_line) + html_line.index('Mar') + 4 + 2] + str(4)
		month = 3
	elif ('Apr' in html_line):
		day = html_line[html_line.index('Apr') + 4:-len(html_line) + html_line.index('Apr') + 4 + 2] + str(4)
		month = 4
	elif ('May' in html_line):
		day = html_line[html_line.index('May') + 4:-len(html_line) + html_line.index('May') + 4 + 2] + str(4)
		month = 5
	elif ('Jun' in html_line):
		day = html_line[html_line.index('Jun') + 4:-len(html_line) + html_line.index('Jun') + 4 + 2] + str(4)
		month = 6
	elif ('Jul' in html_line):
		day = html_line[html_line.index('Jul') + 4:-len(html_line) + html_line.index('Jul') + 4 + 2] + str(4)
		month = 7
	elif ('Aug' in html_line):
		day = int(html_line[html_line.index('Aug') + 4:-len(html_line) + html_line.index('Aug') + 4 + 2]) + int(4)
		month = 8
	elif ('Sep' in html_line):
		day = html_line[html_line.index('Sep') + 4:-len(html_line) + html_line.index('Sep') + 4 + 2] + str(4)
		month = 9
	elif ('Oct' in html_line):
		day = html_line[html_line.index('Oct') + 4:-len(html_line) + html_line.index('Oct') + 4 + 2] + str(4)
		month = 10
	elif ('Nov' in html_line):
		day = html_line[html_line.index('Nov') + 4:-len(html_line) + html_line.index('Nov') + 4 + 2] + str(4)
		month = 11
	elif ('Dec' in html_line):
		day = html_line[html_line.index('Dec') + 4:-len(html_line) + html_line.index('Dec') + 4 + 2] + str(4)
		month = 12
	#No date found
	else:
		day = 1
		month = 1
		year = 2000
	print(day)
	print(web_url)
	assert(int(day) >= 1 and int(day) <= 31)
	
	date = datetime.date(year, month, int(day))
	return date
	
	
#Is given the line of html referring to the specific event
#and the url of the schedules page
#Returns the year the event was played in
def getYear(web_url, html_line):
	#Figure out which year it is based off the URL
	if (MEN_2012 in web_url):
		year = 2011
	elif (MEN_2013 in web_url):
		year = 2012
	elif (MEN_2014 in web_url):
		year = 2013
	elif (MEN_2015 in web_url):
		year = 2014
	elif (WOMEN_2012 in web_url):
		year = 2011
	elif (WOMEN_2013 in web_url):
		year = 2012
	elif (WOMEN_2014 in web_url):
		year = 2013
	elif (WOMEN_2015 in web_url):
		year = 2014
	
	#If the event was in the later months, then the year must be incremented
	if ('Jan' in html_line):
		year += 1
	elif('Feb' in html_line):
		year += 1
	elif('Mar' in html_line):
		year += 1
	elif('Apr' in html_line):
		year += 1
	elif('May' in html_line):
		year += 1
	
	return year

#Gets the latest date of the games in the games.dat file
def getLatestUpdateDate():
	f = open('games.dat', 'r')	
	#Put files into an array
	gameFile = f.readlines()
	#Close file
	f.close()
	#strip each entry in the array of the \n
	gameFile = [x.strip('\n') for x in gameFile]	
		
		
		
	latest_date = datetime.datetime(2000,1,1)
	for g in range(0, len(gameFile)):
		if ('_d' in gameFile[g]):
			date_on_line = str(gameFile[g+1])
			try:
				event_date = datetime.datetime.strptime(date_on_line, '%Y-%m-%d')
				if (event_date > latest_date):
					latest_date = event_date
			except ValueError:
				print "Incorrect format"
			
			
	return latest_date


	

