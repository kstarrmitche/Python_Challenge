import string

def translate(translate1):
	abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o', 'p','q','r','s','t','u','v','w','x','y','z']
	translatedText = ""
	index2 = 0 #index of new translated character

	currentIndex = 0
	#keeps track of our current index
	for letter in translate1:
		if translate1[currentIndex] in string.punctuation or translate1[currentIndex] == ' ':
			translatedText += translate1[currentIndex]
		elif translate1[currentIndex] == 'y':
			translatedText += 'a'
		elif translate1[currentIndex] == 'z':
			translatedText += 'b'
		else:
			index2 = abc.index(translate1[currentIndex])
			translatedText += abc[index2+2]

		currentIndex += 1 

	print(translatedText)

def main():
	#All of this could have been made easier by using the string.maketrans function!!

	translate("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.\
        bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. \
        sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
	translate("map")

main()