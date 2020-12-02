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
	
	charPositions = [int(matches.group(1)), int(matches.group(2))]
	subjectChar = matches.group(3)
	password = matches.group(4)

	print(f'Extracted from string: pos={charPositions[0]},{charPositions[1]}, subjectChar={subjectChar}, password={password}')

	valid = False

	for pos in charPositions:
		if password[pos-1] == subjectChar:
			valid = not valid

	return valid

def countValidPasswords(passwordPolicyStrings):
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

	numValidPasswords = countValidPasswords(testInput)
	print(f'There are {numValidPasswords} valid passwords in the test input')

	testValidPassword = isValid(testInput[0])
	print(f'Test input was {testValidPassword}')

# testInvalidPasswords()

passwordPolicyStrings = readLinesFromFile('./input.txt')
numValidPasswords = countValidPasswords(passwordPolicyStrings)
print(f'There were {numValidPasswords} valid passwords')