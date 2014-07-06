#Is given the html for a page, and decides which URL to visit next
EVENT = "Arial,Helvetica,Geneva"
EVENTLINK = "A HREF="
SCORES = ">Scores</a></td>"
HTTPWORLDCURL = "http://www.worldcurl.com/"
EVENTSURL = "http://www.worldcurl.com/schedule.php?eventtypeid=21&eventyear=2013"
LINESCORE = "linescoredrawlink"
DRAWLINK = "showdrawid"

visitedUrls = []

def getNextPage(html):

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
			if (not hasNotBeenVisitedYet(url[0])):
				return None
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
	return EVENTSURL
					
			
			

#Checks to see if a url has been visited by the crawler already
def hasNotBeenVisitedYet(url):
	if url in visitedUrls:
		return False
	else:
		return True
			

