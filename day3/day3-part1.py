
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
			print(f'moved to {x}, {y}')

			# are the new y cordinate out of bounds?
			# if so adjust them back to the starting edge of the map (or the direction the sled is not moving)
			if y >= (len(map[0])):
				y = y % (len(map[0]))
				print(f'adjusted y = {y}')

			# is there a tree (#) on map[x][y] ?
			if map[x][y] == '#':
				trees += 1
	except IndexError:
		# reached the end of the map
		return trees


def cheapToboggan(current_x, current_y):
	return current_x + 1, current_y + 3


map = readMapFile('input.txt')

print(f'max y={len(map[0])-1} sample: {map[0][len(map[0])-1]}')
numTrees = countTrees(map, cheapToboggan)
print(f'Encountered {numTrees} trees')