
# coding: utf-8

# In[1]:


names = []
tags = []
heads = []
word_tags=[]
sent = ""
s_id=0
sub_id = ""
with open("/home/muskaan/newfiles/HindiWPOST_Parsed47K.txt", "rt") as in_file: #open file
    for line in in_file:
        if(line[0]=="<"):
            if (line[1] == 'S' and line[10]== 'i'):
                s_id = s_id +1;
                sent_id_flag=True
                sub_id = str(s_id)
            else:        
                continue
        elif (line[0] >'0' and line[0]<= '9'):
            if(line[1]=="." or line[2]=="."):
                """                new_index=line.find("\t")
                #                new_index=new_index+1
                                tag_line = line[new_index:]
                                new_index=tag_line.find("\t")
                #                new_index=new_index+1
                                tag_line_half=line[new_index:]
                                new_ending=tag_line_half.find("\t")
                                word_tag=tag_line_half[:new_ending]
                                word_tags.append(word_tag)
                """
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
            outF = open("/home/muskaan/newfiles/HindiHeadExtracted_47K.txt", "a")#exporting output
                # APPENDS (not "writes" so the file needs to be deleted in case of multiple runs of the code are done) line to output file
            if(sent_id_flag):
                sent_id_flag=False
                outF.write("#\nSentence_id:")
                outF.write(sub_id)
                outF.write("\n")
            outF.write("*\t")
            outF.write(tag)
            outF.write("\t")
            outF.write(head)
            outF.write("\n")
            for z in range(len(names)):
                outF.write("@\t")
#                outF.write(word_tags[z])
                outF.write("BLANK\t")
                outF.write(names[z])
                outF.write("\n")
            names = []
            word_tags=[]
            outF.close()
              

            
        
        


# In[3]:


word_tags


# In[ ]:


.+

