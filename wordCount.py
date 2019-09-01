import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists

#source: Daniel Cervantes 9-1-2019
# set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

textFname = sys.argv[1]
outputFname = sys.argv[2]

#first check to make sure program exists
if not os.path.exists("wordCount.py"):
    print ("wordCount.py doesn't exist! Exiting")
    exit()

#make sure text files exist
if not os.path.exists(textFname):
    print ("text file input %s doesn't exist! Exiting" % textFname)
    exit()

#open, read and change all letters to lower case
textFile = open(textFname, 'r').read().lower()

#source: https://www.guru99.com/python-regular-expressions-complete-tutorial.html#7 9-1-2019
#find all words a-z length 1-15, elminiates all other characters
wordList = re.findall(r'\b[a-z]{1,15}\b', textFile)
    

uniqueWords = []
countFrquency = []

# loop through every word in the list
for word in wordList:              
    # Check if word is reoccuring if not add it to the uniqueWords list
    if word not in uniqueWords: 
        #insert new word into the uniqueWords list
        uniqueWords.append(word)

#sort words alphabetically
uniqueWords.sort()

#count the frequency of each word
for i in range(0, len(uniqueWords)):
    countFrquency.append(wordList.count(uniqueWords[i]))

#open output file
outputFile = open(outputFname, "w")

#write results to output 
for i in range(0, len(uniqueWords)):
    outputFile.write("%s %d\n" % (uniqueWords[i], countFrquency[i]))