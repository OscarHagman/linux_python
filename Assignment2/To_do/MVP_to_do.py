import pickle
import datetime
import os

# CONSTANTS
TITLE = 0
TEXT = 1
DATE = 2

TO_DO_LIST = []
error_message = "Invalid input, try again"

# Tries to open saved to-do's, handles if there isn't saved pickle file
try:
    with open("to_do.pickle", "rb") as TO_DO_LIST_pickled:
        LOADED_TO_DO_LIST = pickle.load(TO_DO_LIST_pickled)
    TO_DO_LIST = LOADED_TO_DO_LIST
except FileNotFoundError:
    pass

# FUNCTIONS
def create_to_do() -> list:
    """
    Creates a to-do list with an ID number for the daemon process to have something to refer to.
    :return: A list with the title, text, timestamp and ID number
    """
    while True:
        title_duplicate = False
        title_to_do = input("Enter title: ")
        for items in TO_DO_LIST:
            if title_to_do in items:
                title_duplicate = True
        if title_to_do == "exit":
            print("Title can't be 'exit'")
        elif title_duplicate:
            print("Title", "'" + title_to_do + "'", "already exists")
        else:
            break
    print("Enter to-do text")
    text_to_do = multiline_input()
    date_and_time = str(datetime.datetime.now())[:16]
    return [title_to_do, text_to_do, date_and_time]


def search_to_do(title: str) -> int:
    """
    Will find the index of the desired to-do in the TO_DO_LIST
    :param title: The title of the to-do the user wants to retrieve
    :return: Returns the index for the to-do as an `int`
    """
    for index, to_do in enumerate(TO_DO_LIST):
        if title == to_do[TITLE]:
            return index
    return - 1


def open_to_do(to_do_index: int) -> None:
    """
    Opens the menu for the given to-do which allows the user to read, edit and delete.
    :param to_do_index: The index for what to-do to open
    :return: None
    """

    while True:
        to_do = TO_DO_LIST[to_do_index]
        print("To-do:", to_do[TITLE])
        print("[1] Read\n[2] Edit title & text\n[3] Delete\n[4] Go back")
        to_do_menu_choice = input(": ")
        if to_do_menu_choice == "1":
            print("Title:", to_do[TITLE])
            print("Date created:", to_do[DATE])
            print("\n" + to_do[TEXT] + "\n")
        elif to_do_menu_choice == "2":
            title, text, date = create_to_do()
            TO_DO_LIST[to_do_index] = [title, text, date]

        elif to_do_menu_choice == "3":
            print("You sure you want to delete", to_do[TITLE] + "?")
            if yes_or_no():
                del TO_DO_LIST[to_do_index]
                print(to_do[TITLE], "has been deleted")
                break
        elif to_do_menu_choice == "4":
            print("Going back")
            break
        else:
            print(error_message)


def yes_or_no() -> bool:
    """
    Allows the user to answer simple "yes or no" questions and lets them try again if the input is incorrect
    :return: True for "y" (yes) and False for "n" (no)
    """
    print("(y/n)")
    while True:
        decision = input(": ")
        if decision == "y":
            return True
        elif decision == "n":
            return False
        else:
            print("You can only enter 'y' or 'n', try again")


def input_to_int() -> int:
    """
    Converts user input to an `int` and handles ValueError. Forces the user to try again if it failed
    :return: Integer from user input
    """
    while True:
        try:
            return int(input(": "))
        except ValueError:
            print(error_message)


def multiline_input() -> str:
    """
    Allows the user to input multiple lines of Strings. The user quits by entering an empty String.
    :return: Multiline String
    """
    print("Press 'enter' with no text when you're done\n")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    multiline_text = "\n".join(lines)
    return multiline_text


# PROGRAM STARTS HERE
while True:
    # os.system("clear")
    print("\n[1] Create to-do\n[2] Search to-do\n[3] List to-do's\n[4] Exit")
    main_menu_choice = input(": ")
    if main_menu_choice == "1":
        to_do = create_to_do()
        TO_DO_LIST.append(to_do)
        print("To-do", to_do[TITLE], "has been created")

    elif main_menu_choice == "2":
        if TO_DO_LIST:
            print('enter "exit" to go back')
            title = input("Title: ")
            if title == "exit":
                print("going back")
            else:
                to_do_index = search_to_do(title)
                if to_do_index == - 1:
                    print("Could not find", title)
                else:
                    open_to_do(to_do_index)
        else:
            print("There are no to-do's")

    elif main_menu_choice == "3":
        if TO_DO_LIST:
            while True:
                if not TO_DO_LIST:
                    break
                index_to_do_list = []
                for index, do in enumerate(TO_DO_LIST):
                    index += 1
                    index_to_do_list.append(index)
                    title, text, date = do
                    print("[" + str(index) + "]", title)
                print("[" + str(len(TO_DO_LIST) + 1) + "]", "Go back")

                choose_to_do = input_to_int()
                if choose_to_do in index_to_do_list:
                    open_to_do(choose_to_do - 1)

                elif choose_to_do == len(TO_DO_LIST) + 1:
                    print("Going back")
                    break
                else:
                    print(error_message)
        else:
            print("There are no to-do's")
    elif main_menu_choice == "4":
        with open("to_do.pickle", "wb") as pickle_file:
            pickle.dump(TO_DO_LIST, pickle_file)
        print("Exiting...")
        break
    else:
        print(error_message)
