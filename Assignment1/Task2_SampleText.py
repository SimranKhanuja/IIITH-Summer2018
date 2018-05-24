from xml.dom import minidom
from collections import Counter
import re
unigrams = []
bigrams = []
trigrams = []
probUni = {}
#mydoc = minidom.parse(r'C:\Users\Simran Khanuja\.atom\packages\script\smsCorpus_en_2014.09.06_all.xml')#importing xml file data
#toparse = mydoc.getElementsByTagName('text')#make objects of "text" tag
#for elem in toparse:
#x = elem.firstChild.data.encode('ascii', 'ignore').decode()# get data stored in text tag
x = "I want to eat chinese food"
y = re.findall(r'https?[\.\:\/\w]+|[A-Z][a-z]+(?=[A-Z])|[\'\w\-\$]+|[\,\.\!\@\#\&\*]+',x)# tokenization of the data
unigrams = unigrams + y #update list of unigrams
z = [(y[i],y[i+1]) for i in range(0,len(y)-1)] #make bigram pairs of the tokens
bigrams = bigrams + z #update bigram list
w = [(y[i],y[i+1],y[i+2]) for i in range(0,len(y)-2)] #make trigram tuples of the tokens
trigrams = trigrams + w #update trigram list
countUni= Counter(unigrams) #create a dictionary storing the count of each unigram
countBi = Counter(bigrams)
countTri = Counter(trigrams)
totalUni = sum(countUni.values()) #counting the total number of unigrams
print("Unigram Frequency:\n")
print(countUni)
#for word in countUni:
    #print(word + "\n")
print("Unigram Probability:\n")
for word in countUni.keys():
    wc = countUni.get(word) # getting unigram count
    prob = (wc/totalUni)  #calculating Probability
    probUni.update({word : prob})
    print(word + " : " + str(prob) + "\n")
    #Assigning 0 count to non-existent pairs for bigram frequency count
    for word2 in countUni.keys():
        if((word,word2) not in countBi.keys()):
            countBi.update({(word,word2):0})
totalBi = sum(countBi.values()) #counting the total number of bigrams
print("Bigram Frequency : \n")
print(countBi)
print("Bigram Probability (Conditional) / (Joint) : " +"\n")
for wordpair in countBi.keys():
    wcp = countBi.get(wordpair) #getting bigram count
    probc = (wcp/(countUni.get(wordpair[0]))) #bigram frequency = (count of bigram)/count of first word in the bigram pair
    probj = (probUni.get(wordpair[0])) * (probUni.get(wordpair[1])) #joint prob(x,y) = prob(x) * prob(y)
    print(str(wordpair) + " :  " + str(probc) + "  " + str(probj) + "\n")
    #Assigning 0 count to non-existent pairs for trigram frequency count
    for word in countUni.keys():
        newTri = (wordpair[0],wordpair[1],word)
        if newTri not in countTri.keys():
            countTri.update({newTri : 0})
totalTri = sum(countTri.values()) #counting the total number of trigrams
print("Trigram Frequency : \n")
print(countTri)
print("Trigram Probability  (Conditional) / (Joint): " +"\n")
for word in countTri.keys():
    wc = countTri.get(word)
    if countBi.get((word[0],word[1]))==0:
        probc = 0
    else:
        probc = (wc/countBi.get((word[0],word[1]))) #trigram frequency = (count of trigram)/count of first two words in Trigram
    probj = (probUni.get(word[0])) * (probUni.get(word[1])) * (probUni.get(word[2])) #joint prob(x,y,z) = prob(x) * prob(y) * prob(z)
    print(str(word) + " :  " + str(probc) + "  " + str(probj) + "\n")
