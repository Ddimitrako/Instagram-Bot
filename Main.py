'''Create a note-taking program. When a user starts it up, it should prompt them for a filename.
If they enter a file name that doesn't exist, it should prompt them to enter the text they want to write to the file. After they enter the text, it should save the file and exit.
If they enter a file name that already exists, it should ask the user if they want:
A) Read the file
B) Delete the file and start over
C) Append the file
If the user wants to read the file it should simply show the contents of the file on the screen. If the user wants to start over then the file should be deleted and another empty one made in its place. If a user elects to append the file, then they should be able to enter more text, and that text should be added to the existing text in the file. 

'''
import time
import random
import os
from os.path import exists
fn = input("Enter a filename to read:\n")
fn='comments'
fn+='.txt'
from Instagram_bot import *

login("name","pass") #add the credentials here as login(username,password)
#driver.get(f"https://www.instagram.com/p/CGFbPWSntmr/")

if os.path.isfile(fn):
    print(fn)
    # print the message if file exists
    print("File exists")
    i = input(
        'press 1.Read the file, 2.Delete the file and start over, 3. Append the file: ')
    if i == '1':
        fh = open(fn, 'r',encoding="utf8")        
        for line in fh:            
            print(line)
            comment(f" Message: {line}")
                    
                   
        print("Code stopped because of instagram stoped comments")
        fh.close()
    elif i == '2':
        os.remove(fn)
        print("File Removed!")
    elif i == '3':
        fh = open(fn, 'a',encoding="utf8")
        filedata = input('Append data to file here:')
        fh.write(filedata)
        fh.close()
else:
    print("File does not exist")
    f = open(fn, "w+",encoding="utf8")
    inputdata = input('insert the data for the file here:')
    f.write(inputdata)
    f.close()
