__author__ = 'Craig Cuninghame'
#Python 3.5

import os
import re


#Function to remove a block of text from a file name
def text_remove():
    text_exclude = input("Enter the text to be removed: ")
    continue_on(input("Y or N"))
    for file_name in os.listdir(file_path):
        if text_exclude in file_name:
            destination = os.path.join(file_path, file_name.replace(text_exclude, ""))
            source = os.path.join(file_path, file_name)
            os.rename(source, destination)

#option to continue or break programme
def continue_on(n):
    if n == "Y" or n == "y":
        return
    else:
        exit(0)

#Function to add text to the beginning of a file name
def add_text_beginning():
    text_input = input("Enter the text to be added to the beginning: ")
    continue_on(input("Y or N"))
    for file_name in os.listdir(file_path):
        source = os.path.join(file_path, file_name)
        destination = file_path + "\\" + text_input + file_name
        os.rename(source, destination)

#Function to add text to the end of a file name
def add_text_end():
    text_input = input("Enter the text to be added to the end: ")
    continue_on(input("Y or N"))
    for file_name in os.listdir(file_path):
        length = len(file_name)
        #source = file_path + "\\" + file_name
        source = os.path.join(file_path, file_name)
        extension_length = 0
        for x in file_name:
            if x == ".":
                break
            else:
                extension_length += 1
        extension_length =  length - extension_length
        file_name_no_ext = file_name[0:length - extension_length] #removes the extension
        destination = os.path.join(file_path, file_name_no_ext + " " + text_input + file_name[-extension_length:]) #-4 is the extension
        os.rename(source, destination)


#Function to remove text from end of a file from a certain point
def remove_text_end():
    text_input = input("Enter the text to remove using * as a wildcard: ")
    continue_on(input("Y or N"))
    #add regex in to string
    pattern = re.compile(text_input)
    for file_name in os.listdir(file_path):
        for x in file_name:
            if pattern.match(x):
               print(file_name)



##    for file_name in os.listdir(file_path):
##        if pattern.match(file_name):
##            print(file_name)
##            destination = os.path.join(file_path, file_name.replace(pattern.match(file_name), ""))
##            source = os.path.join(file_path, file_name)
##            os.rename(source, destination)
        




#Function to replace a block of text with another
def replace_text():
    text_removal = input("Enter the text to be removed: ")
    text_replace = input("Enter the text to replace it with: ")
    continue_on(input("Y or N"))
    for file_name in os.listdir(file_path):
        if text_removal in file_name:
            destination = file_path + "\\" + file_name.replace(text_removal, text_replace)
            source = os.path.join(file_path, file_name)
            os.rename(source, destination)


print ("Welcome to Craig's simple file renaming tool!\n\n")
file_path = input("Enter the Path Directory: ")
print ("Printing directory contents: \n")
for item in os.listdir(file_path):
    print (item)
print (""" \n\n
What would you like to do: \n
1. Text Remove Function
2. Add Text to Beginning of File Name
3. Add Text to End of File Name
4. Replace Text within a File Name
5. Delete text using wildcard
""")
choice = input("Please enter your choice: ")
if choice == "1":
    text_remove()
elif choice == "2":
    add_text_beginning()
elif choice == "3":
    add_text_end()
elif choice == "4":
    replace_text()
elif choice == "5":
    remove_text_end()
else:
    print ("Not a valid choice\nBye bye")

print ("\n\n")
for item in os.listdir(file_path):
    print (item)
print ("\n\nComplete")

