import navigator
import retriever
import extractor
import time
import datetime
import shelve



HAMMERTEAM = 0
OTHERTEAM = 1


#Starting URL
URL = 'http://www.worldcurl.com/schedule.php?eventtypeid=21&eventyear=2012'
print("URL: " + URL)
#Crawls the WCT website and extracts all available games
#Stores the information in a local file
def getGames():
	notAllGamesFound = True
	gameData = []
	#Get initial HTML from the starting URL address
	html = retriever.getHTML(URL)

		
	starting_date = getStartingDate()
	
	#Get URL for next page
	url = navigator.getNextPage(html, URL, starting_date)


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
		url = navigator.getNextPage(html, url, starting_date)
		
		
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
	getGames()
	#TODO: Remove Duplicate games
	#removeDuplicates()
	

#Gets the latest date of the games in the games.dat file
def getStartingDate():
	f = open('games.dat', 'r')	
	#Put files into an array
	gameFile = f.readlines()
	#Close file
	f.close()
	#strip each entry in the array of the \n
	gameFile = [x.strip('\n') for x in gameFile]	
		
		
		
	starting_date = datetime.datetime(2000,1,1)
	for g in range(0, len(gameFile)):
		if ('_d' in gameFile[g]):
			date_on_line = str(gameFile[g+1])
			try:
				event_date = datetime.datetime.strptime(date_on_line, '%Y-%m-%d')
				if (event_date >= starting_date):
					starting_date = event_date
			except ValueError:
				print "Incorrect format"
			
			
	return starting_date
	
	
def removeDuplicates():
	f = open('games.dat', 'r')	
	#Put files into an array
	gameFile = f.readlines()
	#Close file
	f.close()
	#strip each entry in the array of the \n
	gameFile = [x.strip('\n') for x in gameFile]
	
	game_date = ''
	game_linescore = ''
	game_skip = ''
	game_event = ''
	
	finished = False
	started = False
	
	
	for g in range(0, len(gameFile)):
		if (finished == True):
			for h in range(g+2, len(gameFile)):
				if (gameFile[h+1] == game_date and \
				gameFile[h+3] == game_linescore and \
				gameFile[h+10] == game_skip and \
				gameFile[h+25] ==  game_event):
					
					print("Duplicate Found on " + g)
		elif ('_d' in gameFile[g]):
			finished = False
			started = True
			game_date = gameFile[g+1]
		elif ('_lh' in gameFile[g]):
			game_linescore = gameFile[g+1]
		elif ('_hs' in gameFile[g]):
			game_skip = gameFile[g+1]
		elif ('_e' in gameFile[g]):
			finished = True
			started = False
			game_event = gameFile[g+1]
		
def gameIsADuplicate:

	

getGames()
		
	
