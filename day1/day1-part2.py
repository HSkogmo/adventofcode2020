# Time: O(n)
# Space: O(n^2)
def twoSumSolve(targetSum, setOfNumbers):
	possibleAnswers = {}

	for number in setOfNumbers:
		x = int(number)
		# is the number in possible answers?
		# if yes, then retrieve the value to that key, and multiply it with "number"
		# if no, continue

		if x in possibleAnswers:
			y = possibleAnswers[x]
			multiplication = x * y
			print('x={}, y={}, x+y={}, x*y={}'.format(x, y, targetSum, multiplication))
			# stop and return on the first identified pair that satifises the targetSum = x + y condition
			return x,y

		y = targetSum - x
		possibleAnswers[y] = x

def readNumbersFromFile(filePath):
	numbers = []
	with open(filePath, 'r') as file:
		for line in file:
			number = int(line)
			numbers.append(number)
	return numbers

# Time: O(n^2)
# Space: O(n^2) ?
# Optimisation ideas; eliminating potential rechecks if there are any?
# 				      sorting the setOfNumbers, and ?
def threeSumSolve(targetSum, setOfNumbers):
	for number in setOfNumbers:
		# targetSum = x + y + z
		x = number
		nestedTargetSum = targetSum - x
		print(f'Solving twoSum for target {nestedTargetSum}')
		try:
			y,z = twoSumSolve(nestedTargetSum, setOfNumbers)
		except TypeError:
			# TypeError occurs when twoSumSolve() didn't return a touple (two values) and Python attempts to unpack it anyway
			# the method returns nothing (or None) when there wasn't a solution to the problem, so we can ignore and continue to the next number
			continue

		# stop and return on the first identified pair that satisfies tha targetSum = x + y + z condition
		print(f'x={x}, y={y}, z={z}, x+y+z={x+y+z}, x*y*z={x*y*z}')
		return x, y, z

nums = readNumbersFromFile('./input.txt')
print('All numbers: {}'.format(nums))

x,y,z = threeSumSolve(2020, nums)