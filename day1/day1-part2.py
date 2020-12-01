def solve():
	possibleAnswers = {}

	with open('./input.txt', 'r') as file:
		for line in file:
			x = int(line)
			# is the number in possible answers?
			# if yes, then retrieve the value to that key, and multiply it with "number"
			# if no, continue

			y = 2020 - x - z

			if x in possibleAnswers:
				y = possibleAnswers[x]
				multiplication = x * y
				print('x={}, y={}, x+y=2020, x*y={}'.format(x, y, multiplication))
				return multiplication

			y = 2020 - x
			possibleAnswers[y] = x

answer = solve()
print(answer)