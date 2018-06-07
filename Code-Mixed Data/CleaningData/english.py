
# coding: utf-8

# In[42]:

import re


# In[1]:

eng=open('Hindi-English-Parallel/IITBombay-parallel/IITB.en-hi.en',encoding='utf-8')


# In[2]:

hin=open('Hindi-English-Parallel/IITBombay-parallel/IITB.en-hi.en',encoding='utf-8')


# In[3]:

content = eng.read().splitlines()  


# In[4]:

content1 = hin.read().splitlines()


# In[33]:

lis=[]
for i in content :
    
    lis.append(" ".join(re.findall("[\w\-\,\.\?]+",i)))
               


# In[34]:

fen=[]
for tr in lis :
    if len(tr)>0 :
        temp=tr.split(' _ ')
        
        temp="".join(temp)
        temp=temp.split(' % ')
        
        temp=" ".join(temp)
        temp=temp.split('% ')
        
        temp="".join(temp)
        temp=temp.split('_ ')
        
        temp="".join(temp)
        temp=temp.split(' s ')
        
        temp=" ".join(temp)
       
        temp=temp.split(' d ')
        
        temp=" ".join(temp)
        
        fen.append(temp)


# In[40]:

new=open('englishIITBombay.txt','w',encoding='utf-8')


# In[41]:

for i in fen :
    new.write(i + "\n")


# In[ ]:



