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
import pandas as pd

def clean_duplicate():
    

    # Replace 'input_file.csv' with the path to your CSV file
    df = pd.read_csv('futurepedia_1.csv')

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Replace 'output_file.csv' with the path to your desired output CSV file
    df.to_csv('removeduplicaterows.csv', index=False)

# clean_duplicate()
from futepedia_Bot import *
# startScrapingUrls()
getDataFromUrl()
# get_all_urls()
# start_Ai() #add the credentials here as login(username,password)
#driver.get(f"https://www.instagram.com/p/CGFbPWSntmr/")


