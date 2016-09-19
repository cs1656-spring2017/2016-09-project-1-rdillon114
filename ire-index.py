import os
import nltk
import json

documents = {}

for filename in os.listdir(os.path.join("input/")):
    f = open('input/' + filename)
    lines = {}
    j = 0
    for line in f:
        lines[j] = line.lower()
        j = j + 1

    documents[filename] = lines

print
print
for key in documents:#for every key in documents, we get the lines, and split them up into individual words.
    lines = documents[key]
    j = 0
    for line in lines:
        words = lines[line].split(" ")
        temp = [0] * len(words)
        i = 0
        for word in words:#words are altered to remove any punctuation and numbers.
            word = word.translate(None, '!?.\'\"\\,()[]{}:;,-_/*@#~1234567890$')
            temp[i] = word
            i = i + 1

        str = ""
        i = 0
        for word in temp:#adding all of the altered words into a temp string, and replacing the original line with the new line, str.
            if i == 0:
                str = word.translate(None, '\n')
                i = i + 1
            else:
                str = str + " " + word.translate(None, '\n ')

        lines[j] = str
        j = j + 1

    documents[key] = lines

porter = nltk.PorterStemmer()

#time to apply stemming to all words in all lines in all documents.
for key in documents:
    lines = documents[key]
    for key1 in lines:
        words = lines[key1].split(" ")
        i = 0
        str = ""
        for word in words:
            if i == 0:
                str = porter.stem(word)
                i += 1
            else:
                str = str + " " + porter.stem(word)
        lines[key1] = str
        #next two lines are for debugging only.
        words = lines[key1]
        print words

#create an inverted index of word counts in documents. first create a list of distinct words, then create x amount of
#dictionaries where x is the number of documents in input/ and initialize all of them to have counts of 0 for each
#distinct word in the documents.

#I am creating the inverted index by making a dictionary of documents that holds dictionaries of words.  To do this,
#I must first make a list of all unique words over all documents.
tempDict = {}

for key in documents:
    lines = documents[key]
    for key1 in lines:
        words = lines[key1].split(" ")
        for word in words:
            tempDict[word] = 0

#now using this temp dictionary, we can initialize a dictionary of words for each document.
#docs is the dictionary of dictionaries that will hold the word counts for all documents.
docs = {}

for key in documents:
    docs[key] = {}

#initializing the word count dictionaries for each document to have a count of 0 for every unique word over all the documents.
for key in docs:
    for word in tempDict:
        docs[key][word] = 0

for key in documents:
    lines = documents[key]
    for key1 in lines:
        words = lines[key1].split(" ")
        for word in words:
            docs[key][word] += 1


#this is for debugging only..... looking at the counts of each word in each document.
for key in docs:
    for word in docs[key]:
        print docs[key][word]

#outputting the docs dictionary to the json file.
file = open("inverted-index.json", "wb")
json.dump(docs, file)
file.close()


'''
print '\n\n\n\n'
for key in docs:
    for key1 in docs[key]:
        print key1
        print docs[key][key1]'''