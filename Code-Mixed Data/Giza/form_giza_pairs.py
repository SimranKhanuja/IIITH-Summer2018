
# coding: utf-8

# In[1]:


eng=open('/home/muskaan/giza pairs/engtohin.txt',encoding='utf-8')


# In[2]:


hin=open('/home/muskaan/giza pairs/hintoeng.txt',encoding='utf-8')


# In[3]:


content=eng.read().split('\n')


# In[4]:


content1=hin.read().split('\n')


# In[5]:


eng.close()
hin.close()


# In[9]:


fcon=[]
for i in content1[:2710425]:
   
    v=[]
    t=i.split(' ')
    if t[2].find("e")==-1:    
        v.append(t[1])
        v.append(t[0])
        v.append(t[2])
        fcon.append(v)

    


# In[10]:


fcon1=[]
for j in content[:2821757]:
    
        
    v=[]
    t=j.split(' ')
    if t[2].find("e")==-1 :
        v.append(t[0])
        v.append(t[1])
        v.append(t[2])
        fcon1.append(v)


# In[12]:


list1=[]
for i in fcon:
    if float(i[2])>0.1:
        list1.append(i)


# In[14]:


list2=[]
for i in fcon1:
    if float(i[2])>0.1:
        list2.append(i)


# In[19]:


f=open('/home/muskaan/giza pairs/hintoeng_0.1.txt',"w",encoding='utf-8')
for x in list1:
    for str in x:
        f.write(str)
        f.write(" ")
    f.write("\n")
f.close()


# In[20]:


f=open('/home/muskaan/giza pairs/engtohin_0.1.txt',"w",encoding='utf-8')
for x in list2:
    for str in x:
        f.write(str)
        f.write(" ")
    f.write("\n")
f.close()


# In[52]:


li1 = []
li2 = []
en=open('/home/muskaan/giza pairs/nicesorteng.txt',encoding='utf-8')
hi=open('/home/muskaan/giza pairs/nicesorthin.txt',encoding='utf-8')
content = en.read().split('\n')
content1 = hi.read().split('\n')
for i in content[:238036]:
   
    v=[]
    t=i.split(' ')
    v.append(t[0])
    v.append(t[1])
    v.append(t[2])
    li2.append(v)
for j in content1[:349244]:
   
    v=[]
    t=j.split(' ')
    v.append(t[0])
    v.append(t[1])
    v.append(t[2])
    li1.append(v)

en.close()
hi.close()


# In[61]:


j=0
prev=0
alignx=[]
aligny=[]
prev_ele="ufnetxkdbhgk"
flag = True
for x in li1:
    flag = True
    if(x[0]==prev_ele):
        continue
    while(flag and j<238036):
        if x[0]==li2[j][0]:
            if x[1]==li2[j][1]:
                prev_ele=x[0]
                flag=False
                prev=j
                alignx.append(x)
                aligny.append(li2[j])
        if(x[0]<li2[j][0]):
            j=prev
            break
        j=j+1

        


# In[70]:


f=open('/home/muskaan/giza pairs/alignx.txt',"w",encoding='utf-8')
for x in alignx:
    for str in x:
        f.write(str)
        f.write(" ")
    f.write("\n")
f.close()


# In[71]:


f=open('/home/muskaan/giza pairs/aligny.txt',"w",encoding='utf-8')
for x in aligny:
    for str in x:
        f.write(str)
        f.write(" ")
    f.write("\n")
f.close()
