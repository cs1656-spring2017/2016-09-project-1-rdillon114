import os

print os.path
lines = {}
l = 'abc@e#g'
l = l.translate(None, '!@#$')
print l

for filename in os.listdir(os.path.join("input/")):
    f = open('input/' + filename)
    for line in f:
        lines[filename] = line.lower()
        print line

print
print
for key in lines:#for every key in lines, we get the line, and split it up into individual words.
    words = lines[key].partition(" ")
    temp = [0] * len(words)
    i = 0
    for word in words:#words are altered to remove any punctuation and numbers.
        word = word.translate(None, '!?.\'\"\\,()[]{}:;,-_/*@#~1234567890')
        temp[i] = word
        i = i + 1

    str = ""
    i = 0
    for word in temp:#adding all of the altered words into a temp string, and replacing the original line with the new line, str.
        if i == 0:
            str = word
            i = i + 1
        else:
            str = str + word

    lines[key] = str

for key in lines:
    print lines[key]
