from paken import scan

samplePass = "?@7"

def cocokan(string):
	if string == samplePass:
		return True
	else:
		False
		
dppass = scan(5, cocokan)

print("passwordnya ialah {0}".format(dppass))