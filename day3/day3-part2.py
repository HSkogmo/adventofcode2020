
def readMapFile(filePath):
	lines = []
	with open(filePath, 'r') as file:
		# file.read().splitlines() removes "\n" from the end of the lines
		for line in file.read().splitlines():
			chars = []
			for char in line:
				chars.append(char)
			lines.append(chars)
	return lines


def countTrees(map, moveToboggan, start_x = 0, start_y = 0):
	trees = 0
	x = start_x
	y = start_y

	# make a move until IndexError occurs which means we've reached the end
	# of the map and can return the tree count
	try:
		while True:
			x, y = moveToboggan(x, y)
			# print(f'moved to {x}, {y}')

			# are the new y cordinate out of bounds?
			# if so adjust them back to the starting edge of the map (or the direction the sled is not moving)
			if y >= (len(map[0])):
				y = y % (len(map[0]))
				# print(f'adjusted y = {y}')

			# is there a tree (#) on map[x][y] ?
			if map[x][y] == '#':
				trees += 1
	except IndexError:
		# reached the end of the map
		return trees

# Method 1
# So many methods for so little gain! Why do they even have names, no one cares!

# def slopeOne(x, y):
# 	return x + 1, y + 1

# def slopeTwo(x, y):
# 	return x + 1, y + 3

# def slopeThree(x, y):
# 	return x + 1, y + 5

# def slopeFour(x, y):
# 	return x + 1, y + 7

# def slopeFive(x, y):
# 	return x + 2, y + 1

# slopes = [slopeOne, slopeTwo, slopeThree, slopeFour, slopeFive]

# Method 2: Anonymous functions, or "lambdas" in python
# Much better :)
slopes = [
	(lambda x,y: (x+1, y+1)),
	(lambda x,y: (x+1, y+3)),
	(lambda x,y: (x+1, y+5)),
	(lambda x,y: (x+1, y+7)),
	(lambda x,y: (x+2, y+1))
]

map = readMapFile('input.txt')

accumulatedProduct = 1
for slope in slopes:
	accumulatedProduct = accumulatedProduct * countTrees(map, slope)

print(f'The accumulatedProduct is {accumulatedProduct}')