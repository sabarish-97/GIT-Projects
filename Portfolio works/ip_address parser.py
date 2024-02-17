import re

def file_update(import_file, remove_list):    # import file consists of allowed IP addresses
    with open(import_file, "r") as file:
        text = file.read()
        print(f"these are the existing allowed IP address {text}")
        text_list = text.split()      # converting text to list

        for element in text_list:
            if element in remove_list
            