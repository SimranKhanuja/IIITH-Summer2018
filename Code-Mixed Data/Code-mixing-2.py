


eng = open('ParsedWithHeadWPOSNew1',encoding='utf-8')
content = eng.read().split("\n")
hin = open("HindiWPOSTLessThan40",encoding='utf-8')
content1 = hin.read().split("\n")
ali = open('greaterthan10perenglish.txt',encoding='utf-8')
alignx = ali.read().split("\n")


# In[40]:


align=[]
for i in alignx:
    t=i.split(" ")
    align.append(t)


# In[57]:


flag = False
flagph = False
phrase = ""
phe = []
phrases = {}
conj = {}
head=[]
headeng={}
for i in content:
    if len(i)>0:
        if i[0]=='S':
            j = i.split(":")[1]
        if i[0]=='@':
            t = i.split("\t")[1]
            if (t=='CC' or t==',') and flag==False:
                phrase = phrase + i.split("\t")[2]
                conj.update({j:i.split("\t")[2]})
                flag = True
            elif flag==True:
                phrase = phrase + " " + i.split("\t")[2]
        if i[0]=='*':
            head.append(i.split("\t")[2])
            if flagph==False:
                flagph = True
            else:
                phe.append(phrase)
                phrase = ""
    
    else:
        if len(phe)>0:
            phe.append(phrase)
            phrase = ""
            headeng.update({j:head})
            phrases.update({j:phe})
            phe = []
            head=[]
        flagph=False
        flag = False

        


# In[61]:


trans = []
transall = []
for x in conj.values():
    for y in align:
        if y[0]==x:
            trans.append(y[1])
    if(len(trans)<=0):
        trans.append(",")
    transall.append(trans)
    trans = []


# In[62]:


phrasehinall = {}
phrasehin = ""
for i,a in enumerate(phrases.keys()):   
    for b in list(content1[int(a)-1].split(" ")):
        if b in transall[i]:
            break
        else:
            phrasehin = phrasehin + b + " "
    phrasehinall.update({a:phrasehin})
    phrasehin = ""


# In[65]:


hind=open('HindiHeadExtracted_final.txt',encoding='utf-8')


# In[66]:


cont=hind.read().split("\n")


# In[67]:


hind.close()


# In[87]:


hindihead={}
hindiheadcopy={}
phraseh=""
phrasehindi={}
headhin=[]
tags=[]
taghin={}
ide=0
ph = []
flag = False
for i in cont[:1000]:
    if len(i)>0:
        if i[0]=='S':
            ide = i.split(":")[1]
        if ide in phrases.keys():
            if i[0]=='@':
                t1 = i.split("\t")
                if len(t1)>2:
                    phraseh = phraseh + " " + t1[2]
                else:
                    phraseh = phraseh + " " + "unknown"
            if i[0]=='*':
                t2 = i.split("\t")
                if len(t2)>2:
                    headhin.append(t2[2])
                else:
                    headhin.append("unknown")
                if flag==False:
                    flag = True
                else:
                    ph.append(phraseh)
                    phraseh = ""
    
    else:
        if ide in phrases.keys():
            ph.append(phraseh)
            phraseh = ""
            hindihead.update({ide:headhin})
            phrasehindi.update({ide:ph})
            #taghin.update({ide:tags})
            headhin = []
            ph=[]
            flag=False


# In[89]:


import copy

hindiheadcopy = copy.deepcopy(hindihead)


# In[90]:


presentinhin = []
presentinhinall = {}
for (i,j) in enumerate(hindihead.values()):
    for (c,x) in enumerate(j):
        if x in list(phrasehinall.values())[i].split(" "):
            presentinhin.append(x)
            list(hindihead.values())[i][c]=""
    presentinhinall.update({i+1:presentinhin})
    presentinhin = []
    


# In[92]:


"""present = []
presentall = {}
for i in headeng.keys():
    for y in headeng.get(i):
        if y in phrases.get(i):
            present.append(y)
    presentall.update({i:present})
    present=[]"""


# In[93]:


"""ls = []
lsall = {}
for i in (headeng.keys()):
    if presentall.get(i):
        for x in presentall.get(i):
            for y in align:
                if y[0]==x:
                    ls.append(y[1])
        lsall.update({i:ls})
        ls =[]"""


# In[94]:


"""final=[]
finalall = {}
for (j,i) in enumerate(hindihead.keys()):
    finalall.update({i:list(set(hindihead.get(i)).intersection(set(lsall.get(i))))})"""    


# In[95]:


"""presentallhin = {}
prehin = []
al = open('alignx.txt',encoding = 'utf-8')
for i in presentall.keys():
    for x in presentall.get(i):
        for j in alignx:
            if x==j.split(" ")[0]:
                prehin.append(j.split(" ")[1])
            else:
                prehin.append("Unknown")
    presentallhin.update({i:prehin})
    prehin = []"""
        
    


# In[96]:


"""indices = []
indicesall = {}
for i in presentallhin.keys():
    for x in presentallhin.get(i):
        for (c,y) in enumerate(x):
            if y in phrasehinall.get(i).split(" "):
                indices.append(c)
    indicesall.update({i:indices})"""
            
    


# In[115]:


trans = []
transall = {}
for i in presentinhinall.keys():
    for j in presentinhinall.get(i):
        for y in align:
            if len(y)>1:
                if y[1]==j:
                    trans.append(y[0])
    transall.update({i:trans})
    trans = []
            
    


# In[119]:


for i in phrases.keys():
    for (c,j) in enumerate(phrases.get(i)):
        for x in j:
            if(transall.get(i)):
                if x in transall.get(i):
                    phrases.get(i)[c] = ""
                    break


# In[122]:


for y in finalall.keys():
    for x in finalall.get(y):
        for (j,z) in enumerate(hindihead.get(y)):
            if z==x:
                hindihead.get(y)[j]=""
            
            


# In[124]:


toappend = []
toappendall = {}
flag = False
extra = ""
for i in (hindihead.keys()):
    for (c,j) in reversed(list(enumerate(hindihead.get(i)))):
        if j=="":
            break
        else:
            toappend.insert(0,phrasehindi.get(i)[c])
    head = hindiheadcopy.get(i)[c]
    for x in phrasehindi.get(i)[c].split(" "):
        if x==head:
            flag=True
        elif flag==True:
            extra = extra + " " + x
    toappend.insert(0,extra)
    toappendall.update({i:toappend})
    toappend = []
    extra = ""
    flag = False


# In[130]:


codemixed = {}
for (i,j) in zip(phrasehinall.keys(),phrases.values()):
    codemixed.update({i:phrasehinall.get(i)+str(j)})


# In[131]:


allcodem = {}
for x in (toappendall.keys()):
    allcodem.update({x:codemixed.get(x) + " ".join(toappendall.get(x))})
    
    
