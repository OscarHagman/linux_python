import functions
from constans import TO_DO_LIST, TITLE, TEXT, ID

TO_DO_ID = 1001
while True:
    print("\n[1] Create to-do\n[2] Search to-do\n[3] List to-do's\n[4] Exit")
    main_menu_choice = input()
    if main_menu_choice == "1":
        while True:
            to_do = functions.create_to_do()

            print("Want to set a reminder?")
            if functions.yes_or_no():
                print("Enter the date and time that you want to be reminded\n'YYYY-MM-DD HH:MM'")
                reminder_date = input(": ")
                functions.set_reminder(reminder_date, TO_DO_ID)

            print("Happy with this to-do?")
            if functions.yes_or_no():
                to_do.append(TO_DO_ID)
                TO_DO_LIST.append(to_do)
                TO_DO_ID += 1
                print("To-do", to_do[0], "has been created")
                break
            else:
                print("Deleted", to_do[TITLE])
                # DELETE REMINDER DAEMON PROCESS
                break
    elif main_menu_choice == "2":
        print('enter "exit" to go back')
        title = input("Title: ")
        if title == "exit":
            print("going back")
        else:
            to_do_index = functions.search_to_do(title)
            if to_do_index == - 1:
                print("Could not find", title)
            else:
                functions.open_to_do(to_do_index)

    elif main_menu_choice == "3":
        if TO_DO_LIST:
            while True:
                if not TO_DO_LIST:
                    break
                index_to_do_list = []
                for index, do in enumerate(TO_DO_LIST):
                    index += 1
                    index_to_do_list.append(index)
                    title, text, date, to_do_id = do
                    print("[" + str(index) + "]", title)
                print("[" + str(len(TO_DO_LIST) + 1) + "]", "Go back")

                choose_to_do = functions.input_to_int()
                if choose_to_do in index_to_do_list:
                    functions.open_to_do(choose_to_do - 1)

                elif choose_to_do == len(TO_DO_LIST) + 1:
                    print("Going back")
                    break
                else:
                    print("error")
        else:
            print("There are no to-dos")
    elif main_menu_choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid input.")
        print("You can choose what to do by entering the number related to the action next to it")
