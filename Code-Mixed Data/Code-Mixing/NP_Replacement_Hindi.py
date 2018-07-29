#Opening files
eng = open('EnglishParsed.txt',encoding='utf-8')
content = eng.read().split("\n")
hin = open('HindiParsed.txt',encoding='utf-8')
content1 = hin.read().split("\n")
eng.close()
hin.close()
content.pop()
content1.pop()


# For extracting information from the parsed files and storing all of them in lists
phrases_hin = []
phrase_tags_hin = []
heads_hin=[]
pos_tags_hin=[]
temp_pos = ""
temp_phrase=""
temp_all_tags=[]
temp_all_heads=[]
temp_all_pos=[]
temp_all_phrases=[]




for i in content1:
    if i[0]=='#':
        temp_all_phrases.append(temp_phrase)
        phrases_hin.append(temp_all_phrases)
        temp_all_pos.append(temp_pos)
        pos_tags_hin.append(temp_all_pos)
        heads_hin.append(temp_all_heads)
        phrase_tags_hin.append(temp_all_tags)
        temp_all_phrases=[]
        temp_all_pos=[]
        temp_phrase=""
        temp_pos = ""
        temp_all_tags=[]
        temp_all_heads=[]
    if i[0]=='*':
        tag=i.split("\t")[1]
        head=i.split("\t")[2]
        if(len(temp_phrase)):
            temp_all_phrases.append(temp_phrase)
            temp_all_pos.append(temp_pos)
        temp_phrase=""
        temp_pos=""
        temp_all_tags.append(tag)
        temp_all_heads.append(head)
    if i[0]=='@':
        temp_phrase = temp_phrase + (i.split("\t")[2]) + " "
        temp_pos = temp_pos + (i.split("\t")[1]) + " "
        
        


phrases_eng = []
phrase_tags_eng = []
heads_eng=[]
temp_all_phrases=[]
temp_phrase=""
temp_all_tags=[]
temp_all_heads=[]


for i in content:
    if i[0]=='#':
        temp_all_phrases.append(temp_phrase)
        phrases_eng.append(temp_all_phrases)
        heads_eng.append(temp_all_heads)
        phrase_tags_eng.append(temp_all_tags)
        temp_all_phrases=[]
        temp_phrase=""
        temp_all_tags=[]
        temp_all_heads=[]
    if i[0]=='*':
        tag=i.split("\t")[1]
        head=i.split("\t")[2]
        if(len(temp_phrase)):
            temp_all_phrases.append(temp_phrase)
        temp_phrase=""
        temp_all_tags.append(tag)
        temp_all_heads.append(head)
    if i[0]=='@':
        temp_phrase = temp_phrase + (i.split("\t")[2]) + " "
        


#Replacing maximum 3 NPs in Hindi sentence with corresponding English NP
#Can change the count to how many ever phrases that you need to replace

newsentences = []
temp_sent = []
replacement_phrase = []

def get_list_from_file(hin_word):
    feng=open('NiceSortEng.txt',encoding='utf-8')
    fhin=open('NiceSortHin.txt',encoding='utf-8')
    line_eng=feng.read().split('\n')
    line_hin=fhin.read().split('\n')

    feng.close()
    fhin.close()

    match=[]
    i=0
    for i in range(len(line_eng)):
        tokens=line_eng[i].split(' ')
        if(tokens[1]==hin_word):
            match.append(tokens[0])
    for i in range(len(line_hin)):
        tokens=line_hin[i].split(' ')
        if(tokens[1]==hin_word):
            match.append(tokens[0])

    return match

flag = False
count = 0
for (i,x) in enumerate(phrase_tags_hin):
    count=0
    for (j,y) in enumerate(x):
        if y=='NP' and count<3:
            flag=False
            head = heads_hin[i][j]
            matches = get_list_from_file(head)
            for (c,z) in enumerate(heads_eng[i]):
                if z in matches:
                    replacement_phrase=phrases_eng[i][c]
                    count = count + 1
                    temp_sent.append(replacement_phrase)
                    flag=True
                    break
            if(flag!=True):
                temp_sent.append(phrases_hin[i][j])
        else:
            temp_sent.append(phrases_hin[i][j])
    newsentences.append(temp_sent)
    temp_sent = []

# For writing into the file :
codemixed = open("CodeMixedHindi.txt",'w',encoding='utf-8')
for i in newsentences:
    codemixed.write(" ".join(x for x in i))
    codemixed.write("\n")
codemixed.close()
