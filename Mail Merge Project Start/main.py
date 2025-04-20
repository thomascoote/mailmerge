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
    #Reads the text
    invite = inv_text.read()
    #Strips out the blank lines that would return \n
    cleaned = invite.strip()
    #Makes a list containing each line of text, seperately
    inv_list = cleaned.splitlines()

#Write out the letters
letters = []
with open("Input/Letters/starting_letter.txt","r") as starting_letter:
    #Reads the text
    letter = starting_letter.read()
    #Number of times to write out a letter. Max index will be total list length -1
    iter_count = len(inv_list)-1
    #Iterate through all items in list
    for i in range (0, iter_count):
        #Writes out the letter replacing [name] with invitee name from list
        new_letter = letter.replace("[name]",inv_list[i])
        #Write out a .txt file in the ReadyToSend folder with the name of the invitee.
        with open(file=f"Output/ReadyToSend/{inv_list[i]}.txt",mode="w") as to_send:
            to_send.write(new_letter)
