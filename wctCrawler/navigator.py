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
WOMEN_2012 = 'http://www.worldcurl.com/schedule.php?eventtypeid=51&eventyear=2012'
WOMEN_2013 = 'http://www.worldcurl.com/schedule.php?eventtypeid=51&eventyear=2013'
WOMEN_2014 = 'http://www.worldcurl.com/schedule.php?eventtypeid=51&eventyear=2014'

visitedUrls = []

def getNextPage(html, web_url):

	#Go through the HTML line by line, check for relevant links
	for line in html:
		#Check for events first
		if (EVENT in line and EVENTLINK in line):
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
					
	#If nothing found, go back to beginning
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


	

