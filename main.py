from openpyxl import Workbook
from openpyxl import load_workbook
import sys
from os import listdir
import os
import worksheetAnalyzer

GETNAME = 1
GETFILENAME = 2
AUTO_LOG = 3
QUIT = 4



#Gets the name of the user
def getName():
	while(True):
		try:
			os.system('clear')
			name = raw_input("What is your name? ");
			return name
		except: 
			raw_input("Error in name.  Press Enter To Continue")
	
		
#Gets the filename that the user wants to log	
def getFileName():
	while(True):	
		try:
			os.system('clear')
			print("What is the name of your document you would like to log automatically? ");
			print("\nPossible Options:")
			xlsFiles = getXLSFiles()
			print(xlsFiles)
			fileName = raw_input("Filename: ");
			if (fileName == 'auto'):
				return xlsFiles[0]
			return fileName
		except (KeyboardInterrupt):
			break
		except (IOError):
			raw_input("Could Not Open File.  Press Enter To Continue");

#Quits the program
def quitProgram():
	os.system('clear')
	print("Goodbye!")
	sys.exit()

#Returns a list of all the xls files in the directory this script is being run
def getXLSFiles():
	
	allFiles = listdir(os.path.dirname(os.path.abspath(__file__)))
	xlsFiles = []
	for xls in range(len(allFiles)):
		if ("xls" in allFiles[xls]): 
			xlsFiles.append(allFiles[xls])
	return xlsFiles

#Calls the worksheet analyzer to fill in the information for the wb	
def auto_log(wb, playerName):
	worksheetAnalyzer.analyzeWorksheet(wb, playerName)

os.system('clear')

print("=====Welcome to the Auto Logger======!\n");

navigation = 1



while(True):
	if(navigation == 0):
		quitProgram()
	if(navigation == GETNAME):
		name = getName()
		if(str(name) == 'back'):
			navigation -= 1
		elif(str(name) == "quit"):
			quitProgram()
		else:
			navigation += 1
	elif(navigation == GETFILENAME):
		fileName = getFileName()
		if (str(fileName) == 'back'):
			navigation -= 1
		elif(str(fileName) == 'quit'):
			quitProgram()
		else:
			try:
				wb = load_workbook(fileName)
				navigation += 1
			except:
				print("Error Loading File")
	elif(navigation == AUTO_LOG):
		print("Auto_logging " + fileName + "...")
		auto_log(wb, name)
		navigation += 1	
	elif(navigation == QUIT):
		quitProgram()

	
	

			
			
