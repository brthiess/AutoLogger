import gameReader
import activityCreator


def analyzeWorksheet(wb, playerName):
	#Returns a list of games 
	games = gameReader.getGames(playerName)
	#Returns the list of practices, workouts, etc.
	#activities activityCreator.getActivities(playerName)
	
	
