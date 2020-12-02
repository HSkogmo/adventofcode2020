import re

def readLinesFromFile(filePath):
	lines = []
	with open(filePath, 'r') as file:
		for line in file:
			lines.append(line)
	return lines

def isValid(passwordPolicyString):
	# string example: 2-9 c: ccccccccc
	# regex: /^([0-9]+)-([0-9]+) (\S): (.+)$/
	matches = re.match(r'^([0-9]+)-([0-9]+) (\S): (.+)$', passwordPolicyString)
	
	minCharCount = int(matches.group(1))
	maxCharCount = int(matches.group(2))
	subjectChar = matches.group(3)
	password = matches.group(4)

	print(f'Extracted from string: min={minCharCount}, max={maxCharCount}, subjectChar={subjectChar}, password={password}')

	charCount = 0
	for char in password:
		if char == subjectChar:
			charCount += 1

	if charCount >= minCharCount and charCount <= maxCharCount:
		return True
	else:
		return False

def countInvalidPasswords(passwordPolicyStrings):
	validPasswordCount = 0
	for passwordPolicyString in passwordPolicyStrings:
		if isValid(passwordPolicyString):
			validPasswordCount += 1
	return validPasswordCount


def testInvalidPasswords():
	testInput = [
		"1-3 a: abcde",
		"1-3 b: cdefg",
		"2-9 c: ccccccccc"
	]

	numInvalidPasswords = countInvalidPasswords(testInput)
	print(f'There are {numInvalidPasswords} invalid passwords in the test input')

passwordPolicyStrings = readLinesFromFile('./input.txt')
numInvalidPasswords = countInvalidPasswords(passwordPolicyStrings)
print(f'There were {numInvalidPasswords} invalid passwords')