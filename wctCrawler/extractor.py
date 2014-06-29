#Is given the HTML for a page, and extracts the relevant information (i.e. linescores)
#from that page.
#Returns a list of games from that page

import datetime

LINESCORE = 'linescoreend'
HAMMERIMG = 'http://www.curlingzone.com/forums/images/hammer.gif'
HAMMER = 'linescorehamer'
ENDOFLINESCORE = '</table><br><br>'
PLAYER = 'playerid'
EVENT = 'meta property="og:title" content='
DATE = 'linescoredrawhead'
YEAR = 'Dates:'



UPPER_TEAM = 1
LOWER_TEAM = 2

UPPER_SKIP = 1
UPPER_THIRD = 2
UPPER_SECOND = 3
UPPER_LEAD = 4
BOTTOM_SKIP = 5
BOTTOM_THIRD = 6
BOTTOM_SECOND = 7
BOTTOM_LEAD = 8

HAMMERTEAM = 0
OTHERTEAM = 1

UKNOWN = 0



def extractInformation(html):
	games = []
	hammer = False
	player_iterator = UNKNOWN
	team_number = UNKNOWN
	year = None
	date = None
	event = None
	
	
	upper_team_has_hammer = False
	
	hammer_team = Team()
	other_team = Team()
	for h in range(0, len(html)):
		#Get the date of the game
		#Need to get year first
		if (YEAR in html[h]):
			year = getYear(html[h+1])
			assert(year is not None)
		elif (DATE in html[h]):
			assert(year is not None)
			date = getDate(html[h], year)
			assert(date is not None)
		#Get the event name
		elif(EVENT in html[h]):
			event = getEvent(html[h])
		#Check if the team has hammer
		elif (HAMMER in html[h] and HAMMERIMG in html[h]):
			hammer = True
		elif(HAMMER in html[h] and HAMMERIMG not in html[h]):
			hammer = False
		#Go through HTML and check for a linescore line
		elif(LINESCORE in html[h]):				
			#Found a linescore line.  Split up the line so that the numbers are separated
			linescores = html[h].split("&nbsp;")	
			
			#Increment the team number.  Used to keep track of 
			#whether this linescore is the top or bottom one
			team_number += 1
			
			#If this is the top linescore, and they have hammer, then note it (used later)
			if (team_number == 1 and hammer == True):
				upper_team_has_hammer = True
			#Create an empty linescore to be filled
			linescore = [[]*8 for x in xrange(8)]
			end_number = 0
			#Go through the linescore and check for scores
			for l in linescores:
				#Check if it is an actual score and not some other random html
				if(len(l) == 1 and ((int(l) >= 0 and int(l) <= 8) or l == 'X')):
					if (hammer == True):
						linescore[HAMMERTEAM][end_number] = l
					elif(hammer == False):
						linescore[OTHERTEAM][end_number] = l
					end_number += 1
						
		#If a player line was found			
		elif(PLAYER in html[h]):
			#Increment this each time a new player is found
			player_position_iterator += 1
			#Update both teams
			hammer_team, other_team = addPlayer(html, h, player_position_iterator, upper_team_has_hammer, hammer_team, other_team)
				
		#Found end of linescore.  Create a game out of it			
		elif(ENDOFLINESCORE in h):
			assert (hammer_team.player_count == 4)
			assert (other_team.player_count == 4)
			assert (date is not None)
			assert (event is not None)
			games.append(Game(date, linescore, hammer_team, other_team, event))
			hammer = False
			team_number = 0
			upper_team_has_hammer = False
			
			

def addPlayer(html, h, position, upper_team_has_hammer, hammer_team, other_team):			
			assert (position >= UPPER_SKIP and position <= BOTTOM_LEAD)
			#Extract the player name from HTML
			#Gets rid of useless html stuff
			player_name = html[h+2].replace("<td><b>", " ").replace("<br>", " ").replace("</b></td>", " ").split()
			
			#Series of if statements to add player to team
			if (upper_team_has_hammer):
				if (position == UPPER_SKIP):
					hammer_team.addPlayer(UPPER_SKIP, player_name)
				elif(position == UPPER_THIRD):
					hammer_team.addPlayer(UPPER_THIRD, player_name)
				elif(position == UPPER_SECOND):
					hammer_team.addPlayer(UPPER_SECOND, player_name)
				elif(position == UPPER_LEAD):
					hammer_team.addPlayer(UPPER_LEAD, player_name)
				elif(position == BOTTOM_SKIP):
					other_team.addPlayer(BOTTOM_SKIP, player_name)
				elif(position == BOTTOM_THIRD):
					other_team.addPlayer(BOTTOM_THIRD, player_name)
				elif(position == BOTTOM_SECOND):
					other_team.addPlayer(BOTTOM_SECOND, player_name)
				elif(position == BOTTOM_LEAD):
					other_team.addPlayer(BOTTOM_LEAD, player_name)
			else:
				if (position == UPPER_SKIP):
					other_team.addPlayer(UPPER_SKIP, player_name)
				elif(position == UPPER_THIRD):
					other_team.addPlayer(UPPER_THIRD, player_name)
				elif(position == UPPER_SECOND):
					other_team.addPlayer(UPPER_SECOND, player_name)
				elif(position == UPPER_LEAD):
					other_team.addPlayer(UPPER_LEAD, player_name)
				elif(position == BOTTOM_SKIP):
					hammer_team.addPlayer(BOTTOM_SKIP, player_name)
				elif(position == BOTTOM_THIRD):
					hammer_team.addPlayer(BOTTOM_THIRD, player_name)
				elif(position == BOTTOM_SECOND):
					hammer_team.addPlayer(BOTTOM_SECOND, player_name)
				elif(position == BOTTOM_LEAD):
					hammer_team.addPlayer(BOTTOM_LEAD, player_name)
					
			return hammer_team, other_team
			
def getYear(html_line):
	for year in range(2008, 2016):
		if (str(year) in html_line):
			return year
	return None
			
def getDate(html_line, year):
	month = 0
	day = 0
	#Check which month is indicated on the line
	if ('Jan' in html_line):
		#Somewhat obtuse line of code here...
		#Grabs the day number (1 - 31), from finding the index of substring of the month
		day = html_line[html_line.index('Jan') + 4:-len(html_line) + html_line.index('Jan') + 4 + 2]
		month = 1
	elif ('Feb' in html_line):
		day = html_line[html_line.index('Feb') + 4:-len(html_line) + html_line.index('Feb') + 4 + 2]
		month = 2
	elif ('Mar' in html_line):
		day = html_line[html_line.index('Mar') + 4:-len(html_line) + html_line.index('Mar') + 4 + 2]
		month = 3
	elif ('Apr' in html_line):
		day = html_line[html_line.index('Apr') + 4:-len(html_line) + html_line.index('Apr') + 4 + 2]
		month = 4
	elif ('May' in html_line):
		day = html_line[html_line.index('May') + 4:-len(html_line) + html_line.index('May') + 4 + 2]
		month = 5
	elif ('Jun' in html_line):
		day = html_line[html_line.index('Jun') + 4:-len(html_line) + html_line.index('Jun') + 4 + 2]
		month = 6
	elif ('Jul' in html_line):
		day = html_line[html_line.index('Jul') + 4:-len(html_line) + html_line.index('Jul') + 4 + 2]
		month = 7
	elif ('Aug' in html_line):
		day = html_line[html_line.index('Aug') + 4:-len(html_line) + html_line.index('Aug') + 4 + 2]
		month = 8
	elif ('Sep' in html_line):
		day = html_line[html_line.index('Sep') + 4:-len(html_line) + html_line.index('Sep') + 4 + 2]
		month = 9
	elif ('Oct' in html_line):
		day = html_line[html_line.index('Oct') + 4:-len(html_line) + html_line.index('Oct') + 4 + 2]
		month = 10
	elif ('Nov' in html_line):
		day = html_line[html_line.index('Nov') + 4:-len(html_line) + html_line.index('Nov') + 4 + 2]
		month = 11
	elif ('Dec' in html_line):
		day = html_line[html_line.index('Dec') + 4:-len(html_line) + html_line.index('Dec') + 4 + 2]
		month = 12
	
	assert(int(day) >= 1 and int(day) <= 31)
	
	date = datetime.date(year, month, int(day))
	return date

def getEvent(html_line):
	event = html_line.replace('<meta property="og:title" content="', "").replace('"/>', "")
	return event
	
			
					
