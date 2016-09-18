import os

print os.path
documents = {}
l = 'abc@e#g'
l = l.translate(None, '!@#$')
print l

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

for key in documents:
    lines = documents[key]
    for key1 in lines:
        words = lines[key1].split(" ")
        for word in words:
            print word

#create an inverted index of word counts in documents. first create a list of distinct words, then create x amount of
#dictionaries where x is the number of documents in input/ and initialize all of them to have counts of 0 for each
#distinct word in the documents.