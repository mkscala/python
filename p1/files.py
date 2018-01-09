#!/usr/bin/env python3
#          8 : Reading / Writing Files
# https://www.youtube.com/watch?v=EukxMIsNeqU&index=8&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt
# http://www.newthinktank.com/2016/07/learn-program-8/

# ---------- READING & WRITING TEXT ----------
'''
cd .git
ls -a | less      list hidden files scroll either up or down using 
the arrow keys 
or you can scroll down one page at a time with the space bar
     dddd

rm -rf .<file-name/directory-name>  delete a single file or directory
'''       
from sys import argv
from os.path import exists
script, filename = argv


txt = open(filename)
print ("Here's your file %r:\n\n\n-------------------------\n\n" % filename)
print (txt.read())


# Text is stored using unicode where numbers represent
# all possible characters

# Open the file for writing
with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    # You can write to the file with write
    # It doesn't add a newline
    myFile.write("Some random text\n  More random text\n  And some more")

# Open the file for reading
# You don't have to provide a mode because it is
# read by default
with open("mydata.txt", encoding="utf-8") as myFile:
    # We can read data in a few ways
    # 1. read() reads everything into 1 string
    # 2. readline() reads everything including the first newline
    # 3. readlines() returns a list of every line which includes
    # each newline

    # Use read() to get everything at once
    print(myFile.read())

# Find out if the file is closed
print("Is file {} closed ==> {}".format(myFile.name,myFile.closed))

# Get the file name
print("myFile.name ==> ",myFile.name)

# Get the access mode of the file
print("access mode = ",myFile.mode)

# Rename our file
#os.rename("mydata.txt", "mydata2.txt")

# Delete a file
# os.remove("mydata.dat")

# Create a directory
# os.mkdir("mydir")

# Change directories
# os.chdir("mydir")

# Display current directory
# print("Current Directory :", os.getcwd())

# Remove a directory, but 1st move back 1 directory
# os.chdir("..")
# os.rmdir("mydir")



# ---------- READ ONE LINE AT A TIME ----------
# Read 1 line at a time with readline()

# Open the file
with open("mydata2.txt", encoding="utf-8") as myFile:
    lineNum = 1
    # We'll use a while loop that loops until the data
    # read is empty
    while True:
        line = myFile.readline()
        if not line:     # line is empty so exit
            break
        print("Line", lineNum, " :", line, end="")
        lineNum += 1

# ---------- PROBLEM : ANALYZE THE FILE ----------
# As you cycle through each line output the number of
# words and average word length
'''
Line 1
Number of Words : 3
Avg Word Length : 4.7
Line 2
Number of Words : 3
Avg Word Length : 4.7
'''

with open("mydata2.txt", encoding="utf-8") as myFile:
    lineNum = 1

    while True:
        line = myFile.readline()
        if not line:  # line is empty so exit
            break
        print("Line", lineNum)

        # Put the words in a list using the space as
        # the boundary between words
        wordList = line.split()

        # Get the number of words with len()
        print("Number of Words :", len(wordList))

        # Incremented for each character
        charCount = 0

        for word in wordList:
            for char in word:
                charCount += 1

        # Divide to find the answer
        avgNumChars = charCount / len(wordList)

        # Use format to limit to 2 decimals
        print("Avg Word Length : {:.2}".format(avgNumChars))

        lineNum += 1

# Reading and Writing Files  58   'learn python the hard way'


target = open(filename, 'w')

print ("Truncating the file. Goodbye!")
target.truncate()   #erase  content of file


target.write('lifghfgg\n hfghfghfghfgh\n ne1')
target.write("\n") 
target.close()


# More Files  62  ex17.py  'learn python the hard way'

