
# coding: utf-8

# In[25]:


names = []
tags = []
heads = []
sent = ""
s_id=0
sub_id = ""
with open("/home/muskaan/newfiles/hindiParsed.txt", "rt") as in_file: #open file
    for line in in_file:
        if(line[0]=="<"):
            if (line[1] == 'S' and line[10]== 'i'):
                s_id = s_id +1;
                sub_id = str(s_id)
            else:        
                continue
        elif (line[0] >'0' and line[0]<= '9'):
            if(line[1]=="." or line[2]=="."):
                index = line.find("name=")
                index = index + 6
                end  = line.find(">")
                temp = line[index:end]
                name_end  = temp.find("'")
                if(name_end>0):
                    name = line[index:index+name_end]
                else:
                    name = line[index:(end-1)]
                names.append(name)
            else:
                tag_index = line.find("(") + 3
                temp_tag = line[tag_index:]
                tag_end = temp_tag.find("\t")
                tag = line[tag_index:(tag_index)+tag_end]
                tags.append(tag)
                
                #finding head
                head_index = temp_tag.find("head")+6
                temp_head = temp_tag[head_index:]
                head_end = temp_head.find("'")
                head = temp_head[:head_end]
                heads.append(head)
        else:
            outF = open("/home/muskaan/newfiles/HindiParsedExtracted.txt", "a")#exporting output
                # APPENDS (not "writes" so the file needs to be deleted in case of multiple runs of the code are done) line to output file
            outF.write("Sentence_id:")
            outF.write(sub_id)
            outF.write("\t")
            outF.write("Tag:")
            outF.write(tag)
            outF.write("\t\t")
            outF.write("Head:")
            outF.write(head)
            outF.write("\t\t")
            outF.write("Phrase:")
            for z in names:
                outF.write(z)
                outF.write(" ")
            names = []
            outF.write("\n")
            outF.close()
              

            
        
        


# In[ ]:


.+

