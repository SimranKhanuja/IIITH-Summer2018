from xml.dom import minidom
from collections import Counter
import re
unigrams = []
bigrams = []
trigrams = []
probUni = {}
probBi = {}
probTri = {}
startProb = {}
start = []
mydoc = minidom.parse(r'C:\Users\Simran Khanuja\.atom\packages\script\smsCorpus_en_2014.09.06_all.xml')#importing xml file data
toparse = mydoc.getElementsByTagName('text')#make objects of "text" tag
for elem in toparse:
    x = elem.firstChild.data.encode('ascii', 'ignore').decode()# get data stored in text tag
    y = re.findall(r'https?[\.\:\/\w]+|[A-Z][a-z]+(?=[A-Z])|[\'\w\-\$]+|[\,\.\!\@\#\&\*]+',x)# tokenization of the data
    if len(y) is not 0:
        start.append(y[0]) #storing the starting words
    unigrams = unigrams + y #update list of unigrams
    z = [(y[i],y[i+1]) for i in range(0,len(y)-1)] #make bigram pairs of the tokens
    bigrams = bigrams + z #update bigram list
    w = [(y[i],y[i+1],y[i+2]) for i in range(0,len(y)-2)] #make trigram tuples of the tokens
    trigrams = trigrams + w #update trigram list
countUni= Counter(unigrams) #create a dictionary storing the count of each unigram
countBi = Counter(bigrams)
countTri = Counter(trigrams)
totalUni = sum(countUni.values()) #counting the total number of unigrams
totalStart = len(start) #counting the total number of start words
for word in start:
    prob = (start.count(word)) / totalStart #finding starting word probabilities
    startProb.update({word:prob})
for word in countUni.keys():
    wc = countUni.get(word) # getting unigram count
    prob = (wc/totalUni)  #calculating Probability
    probUni.update({word : prob})
    #Assigning 0 count to non-existent pairs for bigram frequency count
    """for word2 in countUni.keys():
        if((word,word2) not in countBi.keys()):
            countBi.update({(word,word2):0})"""
totalBi = sum(countBi.values()) #counting the total number of bigrams
for wordpair in countBi.keys():
    wcp = countBi.get(wordpair) #getting bigram count
    probc = (wcp/(countUni.get(wordpair[0]))) #bigram frequency = (count of bigram)/count of first word in the bigram pair
    probBi.update({wordpair : probc})
    #Assigning 0 count to non-existent pairs for trigram frequency count
    """for word in countUni.keys():
        newTri = (wordpair[0],wordpair[1],word)
        if newTri not in countTri.keys():
            countTri.update({newTri : 0})"""
totalTri = sum(countTri.values()) #counting the total number of trigrams
for word in countTri.keys():
    wc = countTri.get(word)
    if countBi.get((word[0],word[1]))==0:
        probc = 0
    else:
        probc = (wc/countBi.get((word[0],word[1]))) #trigram frequency = (count of trigram)/count of first two words in Trigram
    probTri.update({word : probc})
i=0
sentence = []
prob = 1
#NO SMOOTHING - calculating bigram probabilities of 10 randomly generated sentences
while(i<10):
    word = random.choice(unigrams)
    if sentence is empty():
        prob = startUni.get(word)#assigning start word prob to start word
    else:
        if((sentence[len(sentence)-1],word) in bigrams):
            prob = prob * probBi.get(sentence[len(sentence)-1],word)
        else:
            prob = 0   #assigning zero prob to sentence for unrecognized bigram
    sentence = sentence + word
    if word is '.':
        print(sentence + " : " + str(prob))
        sentence = []
        prob = 1
        i = i+1
