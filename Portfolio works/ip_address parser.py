import re

def file_update(import_file, remove_list):    # import file consists of allowed IP addresses
    with open(import_file, "r") as file:
        text = file.read()
        print(f"these are the existing allowed IP address {text}")
        text_list = text.split()      # converting text to list

        for element in text_list:
            if element in remove_list:
                text_list.remove(element)
    
        text = " ".join(text_list)
    with open(import_file, "w") as file:
        file.write(text)

file_update("allow_list.txt", ["192.168.25.60", "192.168.140.81", "192.168.203.198"])

with open("allow.txt", "r") as file:
    text1 = file.read()
print(text1)
            