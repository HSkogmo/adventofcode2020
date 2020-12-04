import re

def in_bound(l, r):
	return lambda x: l <= int(x) <= r

def validate_hgt(height):
	matches = re.match(r'(\d+)(cm|in)', height)
	try:
		# print(f'{matches[0]} | {matches[1]} | {matches[2]}')
		return in_bound(150, 193)(matches[1]) if (matches[2] == 'cm') else in_bound(59, 76)(matches[1])
	except TypeError:
		# TypeError is caused by the matches not returning the expected 3 values
		# This happens when the hgt is `178` and not `178cm`, so it's invalid
		return False

# Optimisation note;
# validate_hcl() and validate_pid() could be made leaner with a validate_regex() to hold the try
# catch logic
def validate_hcl(colour):
	# print(f'{colour}')
	try:
		return re.findall(r'#[0-9a-f]{6}', colour)[0] == colour
	except IndexError:
		# IndexError occurs when trying to get [0] from the regex findall
		# this means that whatever value `colour` was it didn't match the regex pattern
		# so it's not valid
		return False

def validate_pid(pid):
	try:
		return re.findall(r'[0-9]{9}', pid)[0] == pid
	except IndexError:
		return False

class Passport:
	def isValid(self):
		requiredFields = {
			'byr': in_bound(1920, 2002),
			'iyr': in_bound(2010, 2020),
			'eyr': in_bound(2020, 2030),
			'hgt': validate_hgt,
			'hcl': validate_hcl,
			'ecl': (lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
			'pid': validate_pid
		}

		for field in requiredFields:
			# if the attribute was not set on the class
			# or if it was, the method in the value returned False
			if not hasattr(self, field) or not requiredFields[field](getattr(self, field)):
				return False

		return True


def testPassport():
	pp = Passport()
	pp.byr = '1920'
	pp.iyr = '2010'
	pp.eyr = '2020'
	pp.hgt = '75in'
	pp.hcl = '#00000z'
	pp.ecl = '000'
	pp.pid = '000'
	pp.cid = '000'
	print(pp.isValid())


def readPassports(passportFilePath):
	passports = []

	with open(passportFilePath, 'r') as file:
		# instantiate the first passport
		pp = Passport()
		# file.read().splitlines() removes "\n" from the end of the lines
		for line in file.read().splitlines():
			# if the line is empty then we start reading a new passport
			if not line.strip():
				print("empty line detected, recording new passport")
				passports.append(pp)
				pp = Passport()
				continue

			# match on regex to `(\S+):(\S+)` to extract key:values from the line
			matches = re.findall(r'(\S+):(\S+)', line)

			for match in matches:
				print(f'setting attribute {match[0]} to {match[1]}')
				setattr(pp, match[0], match[1])

		# add the last passport
		passports.append(pp)

	return passports


def countValidPassports(passports):
	numValid = 0
	for pp in passports:
		if pp.isValid():
			numValid += 1
	return numValid

passports = readPassports('input.txt')
numValid = countValidPassports(passports)
print(f'Found {numValid} valid passports')

# testPassport()