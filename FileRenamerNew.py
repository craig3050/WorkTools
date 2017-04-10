import re
import os

#These 3 modules are part of the text replace / delete feature
#It takes an argument, matches, then renames the file.
def text_modify(file_path):
    text_removal = input("Enter the text to be removed (use * for wildcard): ")
    text_replace = input("Enter the text to replace it with (press enter if delete only): ")
    continue_on(input("Y or N"))
    for file_name in os.listdir(file_path):
        text_removal_edit = ""
        text_removal_edit = change_to_regex_format(text_removal)
        text_removal_edit = regex_match(text_removal_edit, file_name)
        print (text_removal_edit)
        if text_removal_edit == 0:
            print("no change")
        if text_removal_edit in file_name:
            new_file_name = file_name.replace(text_removal_edit, text_replace)
            file_rename(file_path, file_name, new_file_name)


def change_to_regex_format(input_string):
    output_string = ""
    for letter in input_string:
        if letter == "*":
            output_string += "[\w\W]"
        if letter == "(":
            output_string += "("
        if letter == ")":
            output_string += ")"
        else:
            output_string += letter
    return output_string

def regex_match(input_string, comparison_string):
    match_string = re.compile(input_string)
    print (match_string)
    return_string = match_string.search(comparison_string)
    if return_string == None:
        return 0
    else:
        return return_string.group()


#Module to rename a file taking file path and source & destination names
def file_rename(file_path, source_name, destination_name):
    source = os.path.join(file_path, source_name)
    destination = os.path.join(file_path, destination_name)
    os.rename(source, destination)

#Option to continue or break programme
def continue_on(n):
    if n == "Y" or n == "y":
        return
    else:
        exit(0)


#Main loop. Mainly the menu
def main():
    print ("Welcome to Craig's simple file renaming tool!\n\n")
    file_path = input("Enter the Path Directory: ")
    print ("Printing directory contents: \n")
    for item in os.listdir(file_path):
        print (item)
    print (""" \n\n
    What would you like to do: \n
    1. Text Remove / Replace Function
    2. Add Text to Beginning of File Name
    3. Add Text to End of File Name
    """)
    choice = input("Please enter your choice: ")
    if choice == "1":
        text_modify(file_path)
    elif choice == "2":
        add_text_beginning()
    elif choice == "3":
        add_text_end()
    else:
        print ("Not a valid choice\nBye bye")

    print ("\n\n")
    for item in os.listdir(file_path):
        print (item)
    print ("\n\nComplete")

#Used if run as a standalone script. My attempt ag good practice. 
if __name__ == "__main__":
    main()
