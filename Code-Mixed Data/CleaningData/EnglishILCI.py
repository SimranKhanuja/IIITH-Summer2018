
# coding: utf-8

# Getting English Sentences : ILCI-Corpus

sentences = []
sent = ""
with open("/home/user/Desktop/Code-Mixed Data/Hindi-English-Parallel/ILCI-Corpus/POS-Tagged-English/EnglishICLI.txt", "rt") as in_file: #open file
    for line in in_file: # store each line as a string variable
        if line is '\n':
            sentences.append(sent) #storing senetnces
            sent = ""
        else:
            index = line.find('\t') #separating word from the pos tag
            if line[0] is "." : 
                continue
            else:
                sent = sent + line[0:int(index)] + " " #appending word to make sentence
outF = open("/home/user/Desktop/Code-Mixed Data/Hindi-English-Parallel/ILCI-Corpus/POS-Tagged-English/EnglishSentences.txt", "w")#exporting output
for line in sentences:# write line to output file
    outF.write(line)
    outF.write("\n")
outF.close()
