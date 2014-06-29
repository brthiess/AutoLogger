import navigator
import retriever
import extractor



#Starting URL
URL = 'http://www.worldcurl.com/schedule.php?eventtypeid=21&eventyear=2013'
#Crawls the WCT website and extracts all available games
#Stores the information in a local file
def getGames():
	notAllGamesFound = True
	gameData = []
	#Get initial HTML from the starting URL address
	html = retriever.getHTML(URL)
	#Get URL for next page
	url = navigator.getNextPage(html)

	while(url is not None):
		#Get the HTML source from the URL
		html = retriever.getHTML(url)
		print(url)
		#Get the game data and add it to previous game data
		#gameData.extend(extractor.extractInformation(html))
		#Get URL for next page
		url = navigator.getNextPage(html)
		


getGames()
		
	
