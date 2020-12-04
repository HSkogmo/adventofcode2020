import re

def in_bound(l, r):
	return lambda x: l <= int(x) <= r


class Passport:
	def isValid(self):
		requiredFields = {
			'byr': in_bound(1920, 2002),
			'iyr': in_bound(2010, 2020),
			'eyr': in_bound(2020, 2030),
			'hgt': (lambda x: True),
			'hcl': (lambda x: True),
			'ecl': (lambda x: True),
			'pid': (lambda x: True)
		}

		for field in requiredFields:
			if not hasattr(self, field):
				return False
			else:
				if not requiredFields[field](getattr(self, field)):
					return False

		return True


def testPassport():
	pp = Passport()
	pp.byr = '000'
	pp.iyr = '000'
	pp.eyr = '000'
	pp.hgt = '000'
	pp.hcl = '000'
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
