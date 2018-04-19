from paken import scan

#samplePass = "?@7"
samplePass = "???"
#samplePass = "??"
#samplePass = "bb"
#samplePass = ">??"
#samplePass = "777"

def cocokan(string):
	#print(string)
	if string == samplePass:
		return True
	else:
		False
		
dppass = scan(3, cocokan)

print("passwordnya ialah {0}".format(dppass))