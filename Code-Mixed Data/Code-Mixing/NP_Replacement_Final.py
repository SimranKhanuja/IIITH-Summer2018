# Opening the files, format specified in readme, code to align sentences


hin = open('hindi_aligned (1).txt',encoding='utf-8')
hin1 = open('HindiHeadPOSNew1',encoding='utf-8')
content = hin.read().split("\n")
content1 = hin1.read().split("\n")


# In[245]:


phrases_hin = []
phrase_tags_hin = []
heads_hin=[]
pos_tags_hin=[]
temp_all_phrases=[]
temp_phrase=""
temp_all_tags=[]
temp_all_heads=[]
temp_all_pos=[]
sid=1
change_chunk_eng={}
temp_pos = ""


# In[246]:


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
        sid=sid+1
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
        if(i.split("\t")[1]=='INTF' or i.split("\t")[1]=='RP'):
            change_chunk_eng.update({sid:head})


#Alignment obtained in indices---Dictionary where key is the ID of the Hindi sentence and value is the ID of the English Sentence


ls1={}
for (j,i) in enumerate(phrases_hin):
    newstr = ("").join(x for x in i)
    ls1.update({j:newstr[:len(newstr)-3]})


st1 = ""
content1 = []
for i in content:
    x = list(i.split(" "))
    content1.append(x)
content1.pop()


indices = {}
for i in ls1.keys():
    for (c,j) in enumerate(content):
        if ls1.get(i) in j:
            indices.update({i:c})


#Opening files
eng = open('SampleNewAllFinal',encoding='utf-8')
content = eng.read().split("\n")
ali = open('greaterthan10perenglish.txt',encoding='utf-8')
alignx = ali.read().split("\n")
eng.close()
hin.close()
ali.close()


# In[259]:


align=[]
for i in alignx:
    t=i.split(" ")
    align.append(t)


# In[260]:


phrases_eng = []
phrase_tags_eng = []
heads_eng=[]
temp_all_phrases=[]
temp_phrase=""
temp_all_tags=[]
temp_all_heads=[]


# In[261]:


#extracting phrases for english with phrase tags----list(list(list))
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
        


# In[ ]:


phrases_hin = []
phrase_tags_hin = []
heads_hin=[]
pos_tags_hin=[]
temp_all_phrases=[]
temp_phrase=""
temp_all_tags=[]
temp_all_heads=[]
temp_all_pos=[]
sid=1
change_chunk_eng={}
temp_pos = ""


# Extracting phrases for hindi with phrase tags----list(list(list))
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
        sid=sid+1
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
        if(i.split("\t")[1]=='INTF' or i.split("\t")[1]=='RP'):
            change_chunk_eng.update({sid:head})


# In[281]:


new_phrases_eng = []
new_phrase_tags_eng = []
new_heads_eng=[]
new_phrases_hin = []
new_phrase_tags_hin = []
new_heads_hin=[]
new_pos_tags_hin=[]


# Making a new list containing only the aligned sentences info


for i in indices.keys():
    new_phrases_eng.append(phrases_eng[indices.get(i)])
    new_phrase_tags_eng.append(phrase_tags_eng[indices.get(i)])
    new_heads_eng.append(heads_eng[indices.get(i)])
    new_phrases_hin.append(phrases_hin[i])
    new_phrase_tags_hin.append(phrase_tags_hin[i])
    new_heads_hin.append(heads_hin[i])
    new_pos_tags_hin.append(pos_tags_hin[i])




#Replacing maximum 3 NPs in english sentence with corresponding hindi NP
newsentenceseng = []
temp_sent = []
replacement_phrase = []

def get_list_from_file(eng_word):
    feng=open('nicesorteng.txt',encoding='utf-8')
    fhin=open('nicesorthin.txt',encoding='utf-8')
    line_eng=feng.read().split('\n')
    line_hin=fhin.read().split('\n')

    feng.close()
    fhin.close()

    match=[]
    i=0
    for i in range(len(line_eng)):
        tokens=line_eng[i].split(' ')
        if(tokens[0]==eng_word):
            match.append(tokens[1])
    for i in range(len(line_hin)):
        tokens=line_hin[i].split(' ')
        if(tokens[0]==eng_word):
            match.append(tokens[1])

    return match

flag = False
dem_flag = False
psp_flag = False
rp_flag = False
count = 0
for (i,x) in enumerate(new_phrase_tags_eng):
    count=0
    for (j,y) in enumerate(x):
        if y=='NP' and count<3:
            if(psp_flag or rp_flag):
                temp_sent.append(replacement_phrase)
                psp_flag=False
                rp_flag=False
            flag=False
            dem_flag=False
            head = new_heads_eng[i][j]
            matches = get_list_from_file(head)
            for (c,z) in enumerate(new_heads_hin[i]):
                if z in matches:
                    replacement_phrase=new_phrases_hin[i][c]
                    allpos = list(new_pos_tags_hin[i][c].split(" "))
                    if 'DEM' in allpos:
                        dem_flag=True
                        break
                    if allpos[len(allpos)-2] in ['PSP','RP']:
                        psp_flag = True
                        rp_flag = True
                        flag=True
                        new_replacement = ' '.join(replacement_phrase.split(' ')[:-2])
                        break
                    count = count + 1
                    flag=True
                    break
            if(flag!=True):
                temp_sent.append(new_phrases_eng[i][j])
            elif(psp_flag==False and rp_flag==False):
                temp_sent.append(replacement_phrase)
            
        else:
            if((psp_flag or rp_flag)):
                if(y=='VP'):
                    temp_sent.append(new_replacement)
                else:
                    temp_sent.append(replacement_phrase)
                psp_flag=False
                rp_flag = False
            temp_sent.append(new_phrases_eng[i][j])
    if(psp_flag or rp_flag):
        temp_sent.append(replacement_phrase)
        psp_flag=False
        rp_flag = False
    newsentenceseng.append(temp_sent)
    temp_sent = []

