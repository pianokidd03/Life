def make_matrix(matrix=
    [[0, 1, 0], 
    [0, 0, 1], 
    [1, 1, 1]]
    ):
    """Returns the inputted matrix, this function defaults to a glider
    Parameters
    ----------
    matrix: list
        The matrix to set, the default is the seed for the glider shape

    Returns
    ---------
    list
        8x8 2D matrix
    """
    return matrix


def get_cell(matrix, x, y):
    """Validates cell coordinates

    Parameters
    -----------
    matrix: list
            2D matrix
    y: int
            y coordinate
    x: int
            x coordinate

    Returns
    --------
    value: int
        The cell's value. If the cell is in the matrix, the value
        will be either 1 or 0 depending on whether the cell is living or not
        If the cell is not in the matrix, None will be returned
    """
    if (x >= 0) and (y >= 0):
        try:
            value = matrix[x][y]
        except:
            value = None

        return value


def get_neighbours(matrix, x, y):
    """Gets all the inputted cell's neighbours

    Parameters
    -----------
    matrix: list
        2D matrix
    y: int
        y coordinate
    x: int
        x coordinate

    Return
    ------
    neighbours: list
        returns a list with all the values of the neighbouring cells
    """
    return([
        get_cell(matrix, x, y-1),  # up
        get_cell(matrix, x+1, y-1),  # up, right
        get_cell(matrix, x+1, y),  # right
        get_cell(matrix, x+1, y+1),  # down, right
        get_cell(matrix, x, y+1),  # down
        get_cell(matrix, x-1, y+1),  # down, left
        get_cell(matrix, x-1, y),  # left
        get_cell(matrix, x-1, y-1),  # up, left
    ])


def determine_fate(matrix, x, y):
    """Determines wheter the cell inputted cell will live to the next generation
    Rules:
    Any live cell with two or three live neighbours survives.
    Any dead cell with three live neighbours becoems a live cell.
    All otehr live cells die in the next generation. All other dead cells stay dead.

    Parameters
    -----------
    matrix: list
        2D matrix
    y: int
        y coordinate
    x: int
        x coordinate

    Returns
    -------
    fate: str
        The function returns 1 if the cell will live onto the next generation
        0 is returned if te cell will die
    """
    neighbours = get_neighbours(matrix, x, y)
    num_of_live_neighbours = 0
    for num in neighbours:
        if num != None:
            num_of_live_neighbours = num_of_live_neighbours + num
    if get_cell(matrix, x, y) == 1:
        if (num_of_live_neighbours == 2) or (num_of_live_neighbours == 3):
            return 1
        else:
            return 0
    else:
        if num_of_live_neighbours == 3:
            return 1
        else:
            return 0


def next_gen(current_gen):
    """Returns the map of the next generation based on the current generation
    
    Parameters
    ----------
    current_gen: list
        2D matrix

    Returns
    -------
    gen: list
        2D matrix that models the next generation
    """
    gen = []
    for row in current_gen:
        row.insert(0, 0)
        row.append(0)
    dead_row = [0 for cell in current_gen[0]]
    current_gen.insert(0, dead_row)
    current_gen.append(dead_row)
    for x in range(len(current_gen)):
        row = []
        for y in range(len(current_gen[x])):
            row.append(determine_fate(current_gen, x, y))
        gen.append(row)
    return gen

# TODO: strip unnecessary rows of dead cells

# Simple use case:
# ----------------
# current_gen = make_matrix()

# for i in range(10):
#     for row in current_gen:
#         print(row)
#     current_gen = next_gen(current_gen)
