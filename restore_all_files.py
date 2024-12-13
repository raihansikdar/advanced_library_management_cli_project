# import json
# def restore_all_books(all_books):
#      with open("all_books.json","r") as fp:
#           all_books = json.load(fp)
#      return all_books

import os
import json

def restore_all_books(all_books):
    file_path = "all_books.json"
    if not os.path.exists(file_path):
        # If the file doesn't exist, create it with an empty list
        with open(file_path, "w") as fp:
            json.dump([], fp)
        print("File 'all_books.json' created.")
    with open(file_path, "r") as fp:
        all_books = json.load(fp)
    return all_books
