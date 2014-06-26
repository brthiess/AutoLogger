#Is given the html for a page, and decides which URL to visit next
EVENT = "events.php?"
SCORES = ">Scores</a></td>"
HTTPWORLDCURL = "http://www.worldcurl.com/"
LINESCORE = "linescoredrawlink"

visitedUrls = []

def getNextPage(html):

	#Go through the HTML line by line, check for relevant links
	for line in html:
		#Check for events first
		if (EVENT in line):
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
		elif (LINESCORE in line):
			url = line.replace("href='", " ").replace(">", " ").split()
			
			

#Checks to see if a url has been visited by the crawler already
def hasNotBeenVisitedYet(url):
	if url in visitedUrls:
		return False
	else:
		return True
			

