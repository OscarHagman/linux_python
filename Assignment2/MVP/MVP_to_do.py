import MVP_functions
import pickle
from MVP_constants import TO_DO_LIST, TITLE, error_message

"""
    FIXA formate_date_string() SÅ DEN INTE ÄR OVER-ENGINEERED!
"""
try:
    with open("../to_do.pickle", "rb") as TO_DO_LIST_pickled:
        LOADED_TO_DO_LIST = pickle.load(TO_DO_LIST_pickled)
    TO_DO_LIST = LOADED_TO_DO_LIST
except FileNotFoundError:
    pass

while True:
    print("\n[1] Create to-do\n[2] Search to-do\n[3] List to-do's\n[4] Exit")
    main_menu_choice = input()
    if main_menu_choice == "1":
        while True:
            to_do = MVP_functions.create_to_do()

            print("Happy with this to-do?")
            if MVP_functions.yes_or_no():
                TO_DO_LIST.append(to_do)
                print("To-do", to_do[TITLE], "has been created")
                break
            else:
                print("Deleted", to_do[TITLE])
                # DELETE REMINDER DAEMON PROCESS
                break
    elif main_menu_choice == "2":
        if TO_DO_LIST:
            print('enter "exit" to go back')
            title = input("Title: ")
            if title == "exit":
                print("going back")
            else:
                to_do_index = MVP_functions.search_to_do(title)
                if to_do_index == - 1:
                    print("Could not find", title)
                else:
                    MVP_functions.open_to_do(to_do_index)
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

                choose_to_do = MVP_functions.input_to_int()
                if choose_to_do in index_to_do_list:
                    MVP_functions.open_to_do(choose_to_do - 1)

                elif choose_to_do == len(TO_DO_LIST) + 1:
                    print("Going back")
                    break
                else:
                    print(error_message)
        else:
            print("There are no to-do's")
    elif main_menu_choice == "4":
        with open("../to_do.pickle", "wb") as pickle_file:
            pickle.dump(TO_DO_LIST, pickle_file)
        print("Exiting...")
        break
    else:
        print(error_message)
