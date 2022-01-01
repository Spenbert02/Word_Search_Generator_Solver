from word_search import *


def get_word_list():
    """
    gets a list of words from the user
    :return: list of words which only contain lowercase alpha characters
    """

    ret_list = []  # list of words to return
    user_confirmation = "n"  # tracking whether user wants to use the words they inputted
    while not user_confirmation == "y":

        print("\nEnter the words to include in this word search, one at a time. Press enter when done. Example:")
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

        if len(ret_list) > 0:
            print("You entered the words: ")
            for word in ret_list:
                print(word)
            user_confirmation = input("Are these the words you would like to include? (y/n): ")
        else:  # needs at least one word - overrides decision
            print("At least one word must be entered.")
            user_confirmation = "n"

    return ret_list


if __name__ == "__main__":
    print("\n---------- Word Search Generator ----------")

    user_confirmation = "y"
    while user_confirmation == "y":
        grid_width = int(input("\nEnter width of grid: "))
        grid_height = int(input("\nEnter height of grid: "))
        word_list = get_word_list()

        print("\nGenerating word grid...")

        generated_grid, included_words = generate(grid_width, grid_height, word_list)

        print("\nGrid:")
        for i in range(grid_width):
            print("_", end="")
        print()
        print_word_grid(generated_grid)
        for i in range(int(grid_width * (3/2))):
            print("‾", end="")

        if len(included_words) > 0:
            print("\nWords included:", included_words[0], end="")
            for word in included_words[1:]:
                print(",", word, end="")
            print()
        else:
            print("\nNo given words could be included...")

        user_confirmation = input("\nWould you like to generate another word search? (y/n): ")

    print("\nGoodbye...\n---------- Word Search Solver ----------\n")