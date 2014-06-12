from game import Game
import score

def getGames(playerName):
	#Open File
	f = open('sampleGames')
	#Put files into an array
	gameData = f.readlines()
	#Close file
	f.close()
	#strip each entry in the array of the \n
	gameData = [x.strip('\n') for x in gameData]
	
	
	organizedGames = []
	foundPlayer = False
	
	#Goes through the list of games and parses each line
	#and creates game objects for the specified player
	for g in range(0, len(gameData)):
		if gameData[g] == 'player':
			if gameData[g+1] in playerName or playerName in gameData[g+1]:
				player = gameData[g+1]
				foundPlayer = True
		if foundPlayer:
			if gameData[g] == 'date':
				date = gameData[g+1]
			elif gameData[g] == 'location':
				location = gameData[g+1]
			elif gameData[g] == 'event':
				event = gameData[g+1]
			elif gameData[g] == 'opponent':
				opponent = gameData[g+1]
			elif gameData[g] == 'ourScores':
				ourScores = gameData[g+1]
			elif gameData[g] == 'theirScores':
				theirScores = gameData[g+1]
			elif gameData[g] == 'supervision':
				supervision = gameData[g+1]
			elif gameData[g] == 'technicalRating':
				technicalRating = gameData[g+1]
			elif gameData[g] == 'tacticalRating':
				tacticalRating = gameData[g+1]
			elif gameData[g] == 'physicalRating':
				physicalRating = gameData[g+1]
			elif gameData[g] == 'mentalRating':
				mentalRating = gameData[g+1]
			elif gameData[g] == 'overallRating':
				overallRating = gameData[g+1]
			elif gameData[g] == 'comment':
				comment = gameData[g+1]
			elif gameData[g] == 'endgame':
				organizedGames.append(Game(player, date, event, location,
				opponent, score, supervision, technicalRating, tacticalRating,
				physicalRating, mentalRating, overallRating, comment))
				foundPlayer = False
				
	return organizedGames

			
		
		
	
	
	
