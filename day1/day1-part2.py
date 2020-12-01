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
# Space: O(n^3) ?
def threeSumSolve(targetSum, setOfNumbers):
	for number in setOfNumbers:
		# targetSum = x + y + z
		x = number
		nestedTargetSum = targetSum - x
		try:
			print(f'Solving twoSum for target {nestedTargetSum}')
			y,z = twoSumSolve(nestedTargetSum, nums)
			# stop and return on the first identified pair that satisfies tha targetSum = x + y + z condition
			print(f'x={x}, y={y}, z={z}, x+y+z={x+y+z}, x*y*z={x*y*z}')
			return x, y, z
		except TypeError:
			continue

nums = readNumbersFromFile('./input.txt')
print('All numbers: {}'.format(nums))

x,y,z = threeSumSolve(2020, nums)