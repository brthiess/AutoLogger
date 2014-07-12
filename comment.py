good_physical_comments = [\
'Workout #1', \
'Workout #2', \
'Did some bicycling', \
'Went for a quick run', \
'Had a strong leg workout', \
'Felt energized today!', \
'Did workout #1,  Improving my dead lifts', \
'Did workout #1,  Improving my RDLs', \
'Did workout #1,  Getting better at reverse flys', \
'Did workout #1,  Back extensions felt great', \
'Did workout #1,  Form is improving for back extensions', \
'Very tiring, but good bicycling session', \
'Felt pumped up today', \
'Did workout #2', \
'Workout #2', \
'Had a lot of energy today', \
'Was a little tired at the beginning, but pushed through', \
'Felt very motivated today', \
'Felt very zoned in and focused', \
'Had a good warm up which led to a good workout', \
'Felt like I had great form all workout', \
'Put a lot of effort into workint out today', \
'Did day 1 workout, Very tiring, but good bicycling session', \
'Performed day 1 workout, Felt pumped up today', \
'Did day #2', \
'Core workout', \
'Did the core workout, Had a lot of energy today', \
'Did some bicycling, Was a little tired at the beginning, but pushed through', \
'Performed day 1, workout, Felt very motivated today', \
'Performed day 2, felt very zoned in and focused', \
'Performed workout #2, had a good warm up which led to a good workout', \
'Did day #1 workout, felt like I had great form all workout', \
'Cardio workout, put a lot of effort into it']

bad_physical_comments = [\
'Did Erics first workout', \
'Did Erics second workout', \
'Felt a little sore today', \
'Was a little tired', \
'Did not have much energy', \
'Was not as motivated as I should have been today', \
'Could not focus that great', \
'Probably could have put more effort into it', \
'Felt like my form was a little off today', \
'Did workout #1, Felt a little sore today', \
'Did workout #1, Was a little tired', \
'Workout #1, Did not have much energy', \
'Workout #1, Was not as motivated as I should have been today', \
'Tried workout #1, Could not focus that great', \
'Did core workout today, Probably could have put more effort into it', \
'Attempted day 1 workout, Felt like my form was a little off today', \
'Did day #2, Felt a little sore today', \
'Did day #2, Was a little tired', \
'Day #2, Did not have much energy', \
'Workout #2, Was not as motivated as I should have been today', \
'Tried day #2, Could not focus that great', \
'Did bicycle workout today, Probably could have put more effort into it', \
'Attempted day 1 workout, Felt like my form was a little off today']

all_physical_comments = [\
'Workout #1', \
'Workout #2', \
'Did some bicycling', \
'Went for a quick run', \
'Had a strong leg workout', \
'Felt energized today!', \
'Did workout #1,  Improving my dead lifts', \
'Did workout #1,  Improving my RDLs', \
'Did workout #1,  Getting better at reverse flys', \
'Did workout #1,  Back extensions felt great', \
'Did workout #1,  Form is improving for back extensions', \
'Very tiring, but good bicycling session', \
'Felt pumped up today', \
'Did workout #2', \
'Workout #2', \
'Had a lot of energy today', \
'Was a little tired at the beginning, but pushed through', \
'Felt very motivated today', \
'Felt very zoned in and focused', \
'Had a good warm up which led to a good workout', \
'Felt like I had great form all workout', \
'Put a lot of effort into workint out today', \
'Did day 1 workout, Very tiring, but good bicycling session', \
'Performed day 1 workout, Felt pumped up today', \
'Did day #2', \
'Core workout', \
'Did the core workout, Had a lot of energy today', \
'Did some bicycling, Was a little tired at the beginning, but pushed through', \
'Performed day 1, workout, Felt very motivated today', \
'Performed day 2, felt very zoned in and focused', \
'Performed workout #2, had a good warm up which led to a good workout', \
'Did day #1 workout, felt like I had great form all workout', \
'Cardio workout, put a lot of effort into it', \
'Did Erics first workout', \
'Did Erics second workout', \
'Felt a little sore today', \
'Was a little tired', \
'Did not have much energy', \
'Was not as motivated as I should have been today', \
'Could not focus that great', \
'Probably could have put more effort into it', \
'Felt like my form was a little off today', \
'Did workout #1, Felt a little sore today', \
'Did workout #1, Was a little tired', \
'Workout #1, Did not have much energy', \
'Workout #1, Was not as motivated as I should have been today', \
'Tried workout #1, Could not focus that great', \
'Did core workout today, Probably could have put more effort into it', \
'Attempted day 1 workout, Felt like my form was a little off today', \
'Did day #2, Felt a little sore today', \
'Did day #2, Was a little tired', \
'Day #2, Did not have much energy', \
'Workout #2, Was not as motivated as I should have been today', \
'Tried day #2, Could not focus that great', \
'Did bicycle workout today, Probably could have put more effort into it', \
'Attempted day 1 workout, Felt like my form was a little off today']




import random
from constants import *


def getComment(kind, quality):
	assert(quality >= 0 and quality <= 5)
	if (kind == PHYSICAL):
		if (quality < 3):
			random_comment_number = random.randint(1, len(bad_physical_comments) - 1)
			return bad_physical_comments[random_comment_number]
		elif(quality > 3.5):
			random_comment_number = random.randint(1, len(good_physical_comments) - 1)
			return good_physical_comments[random_comment_number]
		else:
			random_comment_number = random.randint(1, len(all_physical_comments) - 1)
			return all_physical_comments[random_comment_number]
			
	return 0
