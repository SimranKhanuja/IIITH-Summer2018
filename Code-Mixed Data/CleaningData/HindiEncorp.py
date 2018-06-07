
# coding: utf-8

# In[9]:

t=open('hindencorp05.plaintext',encoding='utf8')


# In[10]:

content = t.read().splitlines()


# In[13]:

english=[]
hindi=[]
for sentence in content :
    arr=sentence.split('\t')
    e=arr[3]
    h=arr[4]
    english.append(e)
    hindi.append(h)


# In[22]:

feng=open('final eng','w',encoding='utf-8')


# In[23]:

fhin=open('final hin','w',encoding='utf-8')


# In[24]:

for i in english :
    feng.write(i+"\n")


# In[27]:

for i in hindi :
    fhin.write(i+"\n")


# In[ ]:



