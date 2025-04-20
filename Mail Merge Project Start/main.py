#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#TODO-1: Read the file
#TODO-2: Extract names from file and store in list
#TODO-3: Change "[name]" in "starting_letter.txt" to list item
#TODO-4: Repeat until last index
#TODO-5: Save each file in the Output Directory

#1
#Declare Invitee name list
inv_list = []
with open("Input/Names/invited_names.txt") as invites:
    #Read each line in file
    for line in invites:
        str.replace("\n","")
        inv_list.append(line)
