#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
from os import write

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#TODO-1: Read the file
#TODO-2: Extract names from file and store in list
#TODO-3: Change "[name]" in "starting_letter.txt" to list item
#TODO-4: Repeat until last index
#TODO-5: Save each file in the Output Directory

#File of names
with open("Input/Names/invited_names.txt","r") as inv_text:
    invite = inv_text.read()
    cleaned = invite.strip()
    inv_list = cleaned.splitlines()

with open("Input/Letters/starting_letter.txt","r") as starting_letter:
    letter = starting_letter.read()
    iter_count = len(inv_list)
    for i in range (0, iter_count-1):
        new_letter = letter.replace("[name]",inv_list[i])

        with open()