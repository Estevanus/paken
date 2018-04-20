from paken import scan

#samplePass = "?@7"
#samplePass = "???"
samplePass = "heart"
#samplePass = "??"
#samplePass = "bb"
#samplePass = ">??"
#samplePass = "777"


startValue = "heara"

def cocokan(string):
	print(string)
	if string == samplePass:
		return True
	else:
		False
		
dppass = scan(5, cocokan, startValue)

print("passwordnya ialah {0}".format(dppass))