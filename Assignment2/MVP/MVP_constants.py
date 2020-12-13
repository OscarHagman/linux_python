import pickle

TITLE = 0
TEXT = 1
DATE = 2

TO_DO_LIST = []
error_message = "Invalid input, try again"

try:
    with open("to_do.pickle", "rb") as TO_DO_LIST_pickled:
        LOADED_TO_DO_LIST = pickle.load(TO_DO_LIST_pickled)
    TO_DO_LIST = LOADED_TO_DO_LIST
except FileNotFoundError:
    pass
