import random

#Generates Quality ratings (i.e. Numbers from 0 to 5)

def randomQuality(massDist):
	randRoll = random.random() # in [0,1)
	sum = 0
	result = 2.0
	for mass in massDist:
		sum += mass
		if randRoll < sum:
			return result
		result += 0.5
	print("Should not reach here")
	assert(False);
 
