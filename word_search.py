import random

# only legal directions:
RIGHT = (1, 0)
DOWN = (0, 1)
RIGHT_DOWN = (1, 1)
RIGHT_UP = (1, -1)
DIRECTIONS = (DOWN, RIGHT_DOWN, RIGHT, RIGHT_UP)


def get_size(grid):
    """
    returns size of given grid in (width, height) format
    :param grid: grid to get size of
    :return: width, height tuple
    """

    width = len(grid[0])
    height = len(grid)
    return width, height


def print_word_grid(grid):
    """
    displays given word grid by printing to console
    :param grid: grid to print
    :return: null - prints grid to console
    """

    for row in grid:
        for letter in row:
            print(letter, sep="", end="")
        print(end="\n")


def copy_word_grid(grid):
    """
    returns a deep copy of given grid
    :param grid: grid to copy
    :return: deep copy of grid
    """

    ret_grid = []
    for row in grid:
        curr_row = []
        for letter in row:
            curr_row.append(letter)
        ret_grid.append(curr_row)

    return ret_grid


def extract(grid, position, direction, max_len):
    """
    returns string of word in given grid starting at given position, in given direction, of given maximum length
    :param grid: grid to extract letters from
    :param position: first letter to extract
    :param direction: direction to extract letters from position
    :param max_len: maximum number of letters extracted
    :return: string of letters extracted from grid at position, in direction, with max length of max_len
    """

    min_x, min_y = 0, 0
    max_x, max_y = get_size(grid)
    max_x -= 1
    max_y -= 1
    ret_word = ""

    curr_pos = list(position)
    for i in range(max_len):
        # if the current position is within the grid
        if min_x <= curr_pos[0] <= max_x and min_y <= curr_pos[1] <= max_y:
            ret_word += grid[curr_pos[1]][curr_pos[0]]
            curr_pos[0] += direction[0]
            curr_pos[1] += direction[1]

    return ret_word


def show_solution(grid, word, solution):
    """
    prints grid with solution capitalized if given, or message if no solution
    :param grid: grid to show solution for
    :param word: word to capitalize in grid
    :param solution: position, direction pair
    :return: null - solution grid is printed to console
    """

    if isinstance(solution, bool):  # if solution is bool and false
        print(word + " is not found in this word search")
    else:  # if solution is given
        grid_copy = copy_word_grid(grid)
        curr_pos = [solution[0][0], solution[0][1]]
        direction = [solution[1][0], solution[1][1]]
        for i in range(len(word)):
            grid_copy[curr_pos[1]][curr_pos[0]] = grid_copy[curr_pos[1]][curr_pos[0]].upper()
            curr_pos[0] += direction[0]
            curr_pos[1] += direction[1]
        print(word.upper() + " can be found as below")
        print_word_grid(grid_copy)


def find(grid, word):
    """
    returns location and direction of word in grid
    :param grid: grid to find word in
    :param word: string to find in grid
    :return: position, direction tuple if word found, otherwise returns False
    """

    height, width = get_size(grid)
    # iterating through directions
    for direction in DIRECTIONS:
        # iterating through every position
        for j in range(height):
            for i in range(width):
                # checking if position and direction combo is word
                if extract(grid, (i, j), direction, len(word)) == word:
                    return (i, j), direction

    return False


def find_all(grid, words):
    """
    returns solution dictionary for word list in grid
    :param grid: grid to find solutions for
    :param words: list of words to try to find solutions for in grid
    :return: dictionary containing word-solution key-value pairs
    """

    ret_solution_dict = {}
    for word in words:
        ret_solution_dict[word] = find(grid, word)

    return ret_solution_dict


def empty_grid(width, height):
    """
    returns empty grid (all letters are spaces) with given width and height
    :param width: number of columns
    :param height: number of rows
    :return: empty grid
    """

    ret_grid = []
    for i in range(height):
        curr_row = []
        for j in range(width):
            curr_row.append(" ")
        ret_grid.append(curr_row)

    return ret_grid


def can_insert(grid, position, direction, word):
    """
    returns True if word can be inserted into grid in given position and direction, otherwise returns False
    :param grid: grid to fit word into
    :param position: x-y coordinate of first letter of word
    :param direction: direction word extends from position
    :param word: string to try to insert into grid
    :return: True if word can be inserted, False if not
    """

    existing_word = extract(grid, position, direction, len(word))
    if len(word) == len(existing_word):
        for i in range(len(existing_word)):
            if existing_word[i] != " ":
                if existing_word[i] != word[i]:
                    return False  # does not run off board, but existing letters prevent insertion
        return True  # doesn't run off board and no conflicts with existing letters
    else:
        return False  # runs off board


def insert(grid, position, direction, word):
    """
    inserts word into grid at given position and direction (will overwrite existing letters)
    :param grid: word grid
    :param position: position to insert first letter of word at
    :param direction: direction word extends from position
    :param word: string to insert into grid
    :return: null - grid param is modified
    """
    curr_pos = list(position)
    for i in range(len(word)):
        grid[curr_pos[1]][curr_pos[0]] = word[i]
        curr_pos[0] += direction[0]
        curr_pos[1] += direction[1]


def fit_word(grid, word):
    """
    attempts to fit word into grid 100 times - if successful, returns (position, direction). Otherwise, returns False
    :param grid: grid to fit word into
    :param word: string to fit into grid
    :return: (position, direction) if word fits, False if not
    """

    global DIRECTIONS
    grid_width, grid_height = get_size(grid)
    random.seed(None)  # seeding pseudorandom number generator with system time

    for i in range(100):
        rand_position = (random.randrange(0, grid_width, 1), random.randrange(0, grid_height, 1))
        rand_direction = DIRECTIONS[random.randrange(0, 4, 1)]
        if can_insert(grid, rand_position, rand_direction, word):
            return rand_position, rand_direction

    return False  # if solution not found in 100 tries


def generate(width, height, words):
    """
    returns a grid with given width and height containing given words, and a list of all included words
    :param width: width of desired word grid
    :param height: height of desired word grid
    :param words: words to include in word grid
    :return: generated word grid, list of included words
    """

    ret_grid = empty_grid(width, height)
    included_words = []

    # iterating through each word and trying to insert
    for word in words:
        insert_result = fit_word(ret_grid, word)
        if not isinstance(insert_result, bool):
            insert(ret_grid, insert_result[0], insert_result[1], word)
            included_words.append(word)

    # filling empty grid locations
    for row in range(height):
        for column in range(width):
            if ret_grid[row][column] == " ":
                ret_grid[row][column] = chr(random.randrange(97, 123, 1))  # appending random lowercase letter

    return ret_grid, included_words


if __name__ == "__main__":
    pass
