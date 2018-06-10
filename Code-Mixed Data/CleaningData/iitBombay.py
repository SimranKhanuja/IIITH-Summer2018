
# coding: utf-8

# In[2]:

import re


# In[3]:

eng=open('Hindi-English-Parallel/IITBombay-parallel/IITB.en-hi.en',encoding='utf-8')


# In[4]:

hin=open('Hindi-English-Parallel/IITBombay-parallel/IITB.en-hi.hi',encoding='utf-8')


# In[5]:

content = eng.read().splitlines()  


# In[6]:

content1 = hin.read().splitlines()


# In[1]:

numberOfHindiCharacters = 128;
unicodeShift = 0x0900;
hindiAlphabet = [];
for i in range(128) :
    hindiAlphabet.extend("\\u0" + hex(unicodeShift + i)[2:].upper())
hindi=("".join(hindiAlphabet))
st="["+hindi+"\s]+"


# In[21]:

leng=[]
lhin=[]
ty=0
import itertools
for e,h in zip(content,content1):
    ty=ty+1
    lis=""
    tis=""
    if e.find('%')==-1 :
        if e.find('(')==-1 :
            lis=" ".join(re.findall("[\w\s\?\,\.\-\%]+",e))
        
        else :
            lis=" ".join(re.findall("[\w\s\?\,\.\-\%]+(?=\()|(?<=\))[\w\s\?\,\.\-]+",e)) 
    
        if len(lis)<1:
            tis=""
        if h.find('(')==-1:
            tis="".join(re.findall(st,h))
        else :
            tis=" ".join(re.findall(st+"(?=\()|(?<=\))"+st,h))
        if ty==166 :
            print(tis)
        if tis=="":
            lis=""
        if tis==" ":
            lis=""
        
    leng.append(lis)
    lhin.append(tis)
    
        


# In[17]:

feng=[]
for tr in leng :
    if len(tr)>0 :
        temp=tr.split(' _ ')
        
        temp="".join(temp)
        temp=temp.split('% s')
        
        temp="".join(temp)
        temp=temp.split('%   s')
        
        temp="".join(temp)
        temp=temp.split('_ ')
        
        temp="".join(temp)
       
       
        temp=temp.split('%   d')
        
        temp="".join(temp)
        
        feng.append(temp)
        pr=temp.split(" ' ")
        
        temp="'".join(pr)
    else :
        feng.append("")
    


# In[9]:

english=open("IITBombayEng.txt",'w',encoding='utf-8')
hindi=open("IITBombayHin.txt",'w',encoding='utf-8')


# In[10]:

for i in feng:
    english.write(i+"\n")


# In[11]:

for j in lhin :
    hindi.write(j+"\n")


# In[ ]:



