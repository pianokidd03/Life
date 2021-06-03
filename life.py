def set_matrix():
	return ([
		[1, 0, 0, 1],
		[0, 1, 0, 1],
		[1, 0, 0, 0],
		[0, 1, 0, 0],
	])

def get_cell(matrix, y, x):

	if (x >= 0) and (y >= 0):
		try:
			value = matrix[y][x]
		except:
			value = None

		return value


def get_neighbours(matrix, y, x):
	return([
		get_cell(matrix, y-1, x), # up
		get_cell(matrix, y-1, x+1), # up, right
		get_cell(matrix, y, x+1), # right
		get_cell(matrix, y+1, x+1), # down, right
		get_cell(matrix, y+1, x), # down
		get_cell(matrix, y+1, x-1), # down, left
		get_cell(matrix, y, x-1), # left
		get_cell(matrix, y-1, x-1), # up, left
	])
 

def determine_fate(matrix, y, x):
	"""
	Rules:
	Any live cell with two or three live neighbours survives.
	Any dead cell with three live neighbours becoems a live cell.
	All otehr live cells die in the next generation. All other dead cells stay dead.
	"""
	neighbours = get_neighbours(matrix, y, x)
	num_of_live_neighbours = 0
	for num in neighbours:
		if num != None:
			num_of_live_neighbours = num_of_live_neighbours + num
	if get_cell(matrix, y, x) == 1:
		if (num_of_live_neighbours == 2) or (num_of_live_neighbours == 3):
			return 'Live'
		else:
			return 'Dead'
	else:
		if num_of_live_neighbours == 3:
			return 'Live'
		else:
			return 'Dead'

