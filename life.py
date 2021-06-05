def set_matrix():
    """Set a 8x8 matrix for testing purposes

        Returns
        ---------
        list
                8x8 2D matrix
        """
    return ([
        [1, 0, 0, 1],
        [0, 1, 0, 1],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
    ])


def get_cell(matrix, y, x):
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
            value = matrix[y][x]
        except:
            value = None

        return value


def get_neighbours(matrix, y, x):
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
        get_cell(matrix, y-1, x),  # up
        get_cell(matrix, y-1, x+1),  # up, right
        get_cell(matrix, y, x+1),  # right
        get_cell(matrix, y+1, x+1),  # down, right
        get_cell(matrix, y+1, x),  # down
        get_cell(matrix, y+1, x-1),  # down, left
        get_cell(matrix, y, x-1),  # left
        get_cell(matrix, y-1, x-1),  # up, left
    ])


def determine_fate(matrix, y, x):
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
            The function returns 'Live' if the cell will live onto the next generation
            'Dead' is returned if te cell will die
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
