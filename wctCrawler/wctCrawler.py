import navigator
import retriever
import extractor
import time
import datetime


HAMMERTEAM = 0
OTHERTEAM = 1


#Starting URL
URL = 'http://www.worldcurl.com/schedule.php?eventtypeid=21&eventyear=2013'
#Crawls the WCT website and extracts all available games
#Stores the information in a local file
def getGames(last_update_date):
	notAllGamesFound = True
	gameData = []
	#Get initial HTML from the starting URL address
	html = retriever.getHTML(URL)
	#Get URL for next page
	url = navigator.getNextPage(html, URL, last_update_date)

	while(url is not None):
		#Delay for politeness
		time.sleep(1)
		#Get the HTML source from the URL
		html = retriever.getHTML(url)
		print("URL: " + url)
		#Get the game data and add it to previous game data
		gameData.extend(extractor.extractInformation(html))
		#Add the games to the database
		addGames(gameData)
		#Get URL for next page
		url = navigator.getNextPage(html, url, last_update_date)
		
		
def addGames(gameData):	
	gameFile = open('games.dat', 'a')

	
	#Write all information to a file
	for g in gameData:
		#Write the date
		gameFile.write("_d\n")
		gameFile.write(str(g.date) + '\n')
		#Write the linescore
		gameFile.write("_lh\n")
		gameFile.write(str(g.linescore[HAMMERTEAM]) + '\n')
		gameFile.write("_lo\n")
		gameFile.write(str(g.linescore[OTHERTEAM]) + '\n')
		#Write the team with the hammer
		gameFile.write("_ht\n")
		#Write in lead, second, third, skip
		gameFile.write("_hl\n")
		gameFile.write(str(g.hammerTeam.lead) + '\n')
		gameFile.write("_hs\n")
		gameFile.write(str(g.hammerTeam.second) + '\n')
		gameFile.write("_ht\n")
		gameFile.write(str(g.hammerTeam.third) + '\n')
		gameFile.write("_hf\n")
		gameFile.write(str(g.hammerTeam.skip) + '\n')
		gameFile.write("_ot\n")
		#Write in lead, second, third, skip
		gameFile.write("_ol\n")
		gameFile.write(str(g.otherTeam.lead) + '\n')
		gameFile.write("_os\n")
		gameFile.write(str(g.otherTeam.second) + '\n')
		gameFile.write("_ot\n")
		gameFile.write(str(g.otherTeam.third) + '\n')
		gameFile.write("_of\n")
		gameFile.write(str(g.otherTeam.skip) + '\n')
		#Write in event
		gameFile.write("_e\n")
		gameFile.write(str(g.event) + '\n')
	gameFile.close()
		
		
def updateGames():
	last_update_date = getLastUpdateDate()
	getGames()
	

def getLastUpdateDate():
		gameFile = open('games.dat', 'r')
		
	latestDate = datetime.date(2000,1,1)
	for g in range(0, len(gameFile)):
		if ('_d' in gameFile[g]):
			date_on_line = str(gameFile[g+1])
		try:
			dt_start = datetime.strptime(i, '%Y, %m, %d')
			if (date_on_line > latestDate):
				latestDate = date_on_line
		except ValueError:
			print "Incorrect format"
			
			
	return latestDate
	

getGames()
		
	
