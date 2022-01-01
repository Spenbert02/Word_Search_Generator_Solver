from word_search import *


def print_solution_set_grid(grid, solution_dict):
    """
    prints entire word grid with as many given words highlighted as possible
    :param grid: grid to find words in and print
    :param solution_dict: solution set containing locations of letters to be highlighted
    :return: null
    """

    grid_to_print = copy_word_grid(grid)


def get_word_search():
    """
    gets a word grid from the user
    :return: user-entered grid object
    """

    valid_entry = False  # boolean to track validity of user entered grid
    user_grid = []  # grid to fill and return

    while not valid_entry:  # getting grids from the user until valid grid is entered
        print("\nEnter the grid, row by row, and press enter when done. Example:")
        print("a b c\nd e f\ng h i\n<enter>\n")

        valid_entry = True  # assuming entry is valid until it is deemed invalid
        user_grid = []  # resetting for every user iteration
        curr_row = [""]  # current row of user input
        grid_width = 0  # determined by first row of user input
        is_first_iteration = True  # needed by while loop

        while len(curr_row) != 0:  # getting user input row by row
            curr_row = []
            user_input = input()
            for char in user_input:  # appending valid user entered characters to the current row
                if char.isalpha():
                    curr_row.append(char.lower())
            if is_first_iteration:  # establishing necessary grid width from first user entry
                grid_width = len(curr_row)
                is_first_iteration = False
            if len(curr_row) != 0 and len(curr_row) != grid_width:  # checking if the current entered row is valid
                valid_entry = False
                print("Invalid row length - each row must contain the same number of letters.")
                break
            if len(curr_row) != 0:  # if the user didn't signal to stop, append row to user_grid
                user_grid.append(curr_row)

        if valid_entry:  # if the entered grid is valid, ensuring it is the grid the user meant to enter
            print("User entered grid:")
            print_word_grid(user_grid)
            user_confirmation = input("Is this the grid you would like to use? (y/n): ")
            if user_confirmation != "y":
                valid_entry = False

    return user_grid


def get_word_list():
    """
    gets a list of words from the user
    :return: list of words which only contain lowercase alpha characters
    """

    ret_list = []  # list of words to return
    user_confirmation = "n"  # tracking whether user wants to use the words they inputted
    while not user_confirmation == "y":

        print("\nEnter the words to find in this word search, one at a time. Press enter when done. Example:")
        print("cat\ndog\npig\nhorse\n<enter>\n")
        ret_list = []
        curr_word = " "

        while curr_word != "":
            curr_word = ""  # resetting current word
            user_input = input()  # getting input from the user
            for char in user_input:  # filtering out non-alpha characters
                if char.isalpha():
                    curr_word += char.lower()
            if curr_word != "":  # append word to ret_list if isn't empty
                ret_list.append(curr_word)

        print("You entered the words: ")
        for word in ret_list:
            print(word)
        user_confirmation = input("Are these the words you would like to find? (y/n): ")

    return ret_list


def get_solution_grid(grid, solution_dict):
    """
    returns a grid with all solution words in uppercase
    :param grid:
    :param solution_dict:
    :return: grid with all solution words in uppercase
    """

    ret_grid = copy_word_grid(grid)

    for word in solution_dict:  # iterating through each word in solution
        curr_solution = solution_dict[word]
        if not isinstance(curr_solution, bool):  # if a solution exists for word
            curr_pos = list(curr_solution[0])  # grabbing position from current solution
            direction = list(curr_solution[1])  # grabbing direction from current solution
            for char in word:
                ret_grid[curr_pos[1]][curr_pos[0]] = grid[curr_pos[1]][curr_pos[0]].upper()  # capitalize letter
                curr_pos[0] += direction[0]  # increment x position as indicated by direction
                curr_pos[1] += direction[1]  # increment y position as indicated by direction

    return ret_grid


if __name__ == "__main__":
    print("\n---------- Word Search Solver ----------")

    continue_input = "y"
    while continue_input == "y":  # keep solving as many word searches as the user wants
        user_entered_grid = get_word_search()  # getting a word grid from the user
        user_word_list = get_word_list()  # getting a list of words to find from the user

        print("\nFinding words...")
        user_grid_solution = find_all(user_entered_grid, user_word_list)  # using word_search.py to find words

        print("\nWords found:")
        none_found = True
        for word in user_grid_solution:
            if not isinstance(user_grid_solution[word], bool):
                none_found = False
                print(word)
        if none_found:
            print("~~ no words found ~~")

        print("\nSolution: ")
        solution_grid = get_solution_grid(user_entered_grid, user_grid_solution)
        print_word_grid(solution_grid)

        continue_input = input("\nWould you like to solve another word search? (y/n): ")

    print("\nGoodbye...\n---------- Word Search Solver ----------\n")
