import re

def file_update(import_file, remove_list):    # import file consists of allowed IP addresses
    with open(import_file, "r") as file:
        text = file.read()
        print(f"these are the existing allowed IP address {text}")
        text_list = text.split()              # converting string to list

        for element in text_list:             # iteration to check every IP address in the list
            if element in remove_list:
                text_list.remove(element)
    
        text = " ".join(text_list)            # convert list to string
    with open(import_file, "w") as file:
        file.write(text)                      # update the file 

file_update("allow_list.txt", ["192.168.6.9", "192.168.140.81", "192.168.203.198"])

with open("allow_list.txt", "r") as file:     # read the contents of the file
    text1 = file.read()
print(f"please find the updated IP Address details that are allowed")
pattern = "\d+\.\d+\.\d+\.\d+\d"
separated_string = re.findall(pattern, text1) # using regex to split individual IP address
for i in separated_string:                    # using for loop to print IP Address line by line
    print(f"{i}")

            