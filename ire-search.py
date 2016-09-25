__author__ = 'Richard Dillon'


import json
import math
import nltk

#reading in the json file with the inverted index data structure.
f = open('inverted-index.json','rb')
iIndex = json.load(f)
f.close()

porter = nltk.PorterStemmer()
keys = {}
stemkeys = {}
i = 0
f = open("keywords.txt")
for line in f:
    str = line.split(" ")
    st = line.split(" ")
    keys[i] = st
    #applying stemming to keywords here.
    j = 0
    for word in str:
        word = word.lower()
        word = word.translate(None, '!?.\'\"\\,()[]{}:;,-_/*@#~1234567890$\n ')
        word = porter.stem(word)
        str[j] = word
        j = j + 1
    stemkeys[i] = str
    i = i + 1

#calculate the relevance scores and weights of all keywords / documents.
nSubI = {}

#initializing all words in nSubI to 0.
for doc in iIndex:
    words = iIndex[doc]
    for word in words:
        nSubI[word] = 0

#calculating nSubI for every word that could possibly be a keyword.
for doc in iIndex:
    words = iIndex[doc]
    for word in words:
        if words[word] > 0:
            nSubI[word] += 1

#need to account for multiple lines of keywords.  The following code needs to be changed.
for set in stemkeys:
    rankings = {}
    for doc in iIndex:
        words = iIndex[doc]
        weights = {}
        keywords = stemkeys[set]
        for keyword in keywords:
            total = 0
            #might need to initialize TF to 0 if it is supposed to be 0 for files that don't have keyword in them at all.
            try:
                if words[keyword] != 0:
                    total = 1 + math.log(words[keyword], 2)

                total = total * math.log((float(len(iIndex)) / float(nSubI[keyword])), 2)
                # now we get the weight for one of the keywords by multiplying TF and IDF
            except KeyError:
                ''
            x = total
            weights[keyword] = x

        rankings[doc] = weights
        x = 0.0
        for j in weights:
            x += weights[j]

        # getting the overall ranking and saving it in the 'overall' for that document.
        rankings[doc]['overall'] = x


    # Now I need to sort the rankings from highest to lowest.
    sortedRankings = {}
    for doc in rankings:
        sortedRankings[doc] = rankings[doc]['overall']

    sortedRankings = sorted(sortedRankings.items(), key = lambda l: l[1])


    # displaying all ranks from best to worst, and the weights of each keyword. we do this for each set of keywords.
    i = len(iIndex) - 1
    print '------------------------------------------------------------'
    st = ''
    for keyword in keys[set]:
        st = st + ' ' + keyword.translate(None, '\n')
    print 'keywords =' + st
    print
    while i >= 0:
        list1 = sortedRankings[i]
        doc = list1[0]
        weights = rankings[doc]

        print 'file=' + doc + ' score=', rankings[doc]['overall']

        j = 0
        for keyword in keys[set]:
            temp = 'weight('
            temp += keyword.translate(None, '\n')
            temp += ')='
            print temp, weights[stemkeys[set][j]]
            j = j + 1
        print ''

        i = i - 1
