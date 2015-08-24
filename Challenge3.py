#Trying a new approach. Got some hints from http://jenstander.com/2011/01/16/learning-python-with-the-python-challenge-levels-0-6/
#also, using urllib/regex for the first time!
#regex help also from regex101.com
#Also, if I try this again, I probably wouldn't use regex with urllib
#result: b'linkedList
import re
import urllib.request #imports a lib that allows me to fetch the html code from a page
def main():

	with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html') as response: #reads source code from page
		html = response.read()

	#regex a big help here
	print(b''.join(re.findall(b'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', html)))

main()
