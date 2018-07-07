
# coding: utf-8

# In[3]:


code_mixed_sent=[]
sentence_id=1

mixed_file = open('/home/muskaan/code mixed/code_mixed.txt',"w",encoding='utf-8')

# returns list having all the possible translations of the eng_word[i]
def get_list_from_file(eng_word):
    feng=open('/home/muskaan/giza pairs/nicesorteng.txt',encoding='utf-8')
    fhin=open('/home/muskaan/giza pairs/nicesorthin.txt',encoding='utf-8')
    line_eng=feng.read().split('\n')
    line_hin=fhin.read().split('\n')
    
    feng.close()
    fhin.close()
    
    i=0
    match=[]
    for i in range(len(line_eng)):
        tokens=line_eng[i].split(' ')
        if(tokens[0]==eng_word):
            match.append(tokens[1])
        if(tokens[0]>eng_word):
            break
    for i in range(len(line_hin)):
        tokens=line_hin[i].split(' ')
        if(tokens[0]==eng_word):
            match.append(tokens[1])
        if(tokens[0]>eng_word):
            break 
            
    return match


#returns position of the phrase whose head matches with one of the translations returned by the function get_list_from_file
def get_phrase_pos(heads_eng,i,heads_hin):
    flag=False
    j=0
    match_list = get_list_from_file(heads_eng[i])
    for match in match_list:
        for j in range(len(heads_hin)):
            if(match==heads_hin[j]):
                flag=True
                break
        if(flag):
            break    
    if(flag):
        return j
    return -1

#returns translation of eng_word which is present in the heads_hin
def get_translation(eng_word,heads_hin):
    flag=False
    j=0
    match_list = get_list_from_file(eng_word)
    for match in match_list:
        for j in range(len(heads_hin)):
            if(match==heads_hin[j]):
                flag=True
                break
        if(flag):
            break    
    if(flag):
        return j
    return -1
    
#PardsedWithHeadWPOShin/eng must be in a specific format 
eng = open('/home/muskaan/code mixed/ParsedWithHeadWPOS_eng47K.txt',encoding='utf-8')
hin = open('/home/muskaan/code mixed/ParsedWithHeadWPOS_hin47K.txt',encoding='utf-8')

ln_eng1 = eng.read().split('\n')
ln_hin1 = hin.read().split('\n')

ln_eng=ln_eng1[:1000]
ln_hin=ln_hin1[:1000]

eng.close()
hin.close()

#reading and storing english file
c=-1
not1stflag=False
for m in range(len(ln_eng)-1):
#    print("m is",m)
    done_flag=False
    mix_code=False
    if(ln_eng[m]=='#'):
        words_tags_eng.append(temp_tags_eng)
        phrases_eng.append(temp_words_eng)
        done_flag=True
        not1stflag=False
        
    if(ln_eng[m][0]=='S'):
#        split = ln_eng[i].split(':')
#       sent_id = split[1]
        phrase_tags_eng=[]
        heads_eng=[]
        phrases_eng=[]
        words_tags_eng=[]
        temp_words_eng=[]
        temp_tags_eng=[]
        
        
        
    else:
        tokens = ln_eng[m].split('\t')
        if(tokens[0]=='*'):
            if(not1stflag):
                words_tags_eng.append(temp_tags_eng)
                phrases_eng.append(temp_words_eng)
                not1stflag=False
            phrase_tags_eng.append(tokens[1])
            heads_eng.append(tokens[2])
            temp_tags_eng=[]
            temp_words_eng=[]
        if(tokens[0]=='@'):
            not1stflag=True
            temp_tags_eng.append(tokens[1])
            temp_words_eng.append(tokens[2])
        
    if(done_flag==False):
        continue


# reading hindi file the same way
    not1stflag=False
    break_flag=False
    mix_code=False
    c=c+1
    while (c< len(ln_hin) and (mix_code==False)):
#        print("this c ",c)
        if(ln_hin[c]=='#'):
            words_tags_hin.append(temp_tags_hin)
            phrases_hin.append(temp_words_hin)
            not1stflag=False
            mix_code=True
            break
        if (c<len(ln_hin)-1 and ln_hin[c][0]=='S'):
    #        split = ln_eng[i].split(':')
    #       sent_id = split[1]
            c=c+1
#            print(c)


            phrase_tags_hin=[]
            heads_hin=[]
            phrases_hin=[]
            words_tags_hin=[]
            temp_words_hin=[]
            temp_tags_hin=[]



        else:
            tokens = ln_hin[c].split('\t')
            if(tokens[0]=='*'):
                if(not1stflag):
                    words_tags_hin.append(temp_tags_hin)
                    phrases_hin.append(temp_words_hin)
                    not1stflag=False
                phrase_tags_hin.append(tokens[1])
                heads_hin.append(tokens[2])
                temp_tags_hin=[]
                temp_words_hin=[]
            if(tokens[0]=='@'):
                not1stflag=True
                temp_tags_hin.append(tokens[1])
                temp_words_hin.append(tokens[2])
            c=c+1
#            print(c)



    """"phrase_tags_eng=['NP','NP','VP','NP']
    heads_eng=['this','night','scares','me']
    phrases_eng=[['This'],['rainy','night'],['scares'],['me']]
    words_tags_eng=[['DT'],['JJ','NN'],['VBZ'],['PRP']]

    phrase_tags_hin=['NP','NP','NP','VGF']
    heads_hin=['यह','रात','मुझे','डराती']
    phrases_hin=[['यह'],['अँधेरी','रात'],['मुझे'],['डराती','है']]
    words_tags_hin=[['PRP'],['JJ','NN'],['PRP'],['VM','VAUX']]"""

#algorithm for generating code mixed data
    if(mix_code):
        i=0
        k=0
        j=0

        flag=False
        for i in range(len(phrases_eng)):
            append_eng=False
            if (phrase_tags_eng[i]=="ADJP"):
                s=len(words_tags_eng[i])
                if (s==1):
                    if(words_tags_eng[i][0]=="JJ"):
                        j = get_phrase_pos(heads_eng,i,heads_hin)
                        if(j==-1):
                            append_eng=True
                        else:
                            code_mixed_sent.append(heads_hin[j])
                elif(s==2):
                    if words_tags_eng[i][0]=="RBR" and words_tags_eng[i][1]=="JJ":
                        for x in range(len(words_tags_eng[i])):
                            j = get_translation(phrases_eng[i][x],heads_hin)
                            if(j==-1):
                                code_mixed_sent.append(phrases_eng[i][x])
                            else:
                                code_mixed_sent.append(heads_hin[j])
                else:
                    for x in range(len(words_tags_eng[i])):
                        if words_tags_eng[i][x]!="JJ":
                            code_mixed_sent.append(phrases_eng[i][x])
                        else:
                            j = get_translation(phrases_eng[i][x],heads_hin)
                            if(j==-1):
                                code_mixed_sent.append(phrases_eng[i][x])
                            else:
                                code_mixed_sent.append(heads_hin[j])
                    
                """else:
                    for word in phrases_eng[i]:
                        code_mixed_sent.append(word)
                if(append_eng):
                    for word in phrases_eng[i]:
                        code_mixed_sent.append(word)"""
               
                        
                
            elif (phrase_tags_eng[i]=="NP"):
                s=len(words_tags_eng[i])
                if (s==1):
                    if words_tags_eng[i][0]=="DT" or words_tags_eng[i][0]=="PRP" or words_tags_eng[i][0]=="PRP$":
                        code_mixed_sent.append(phrases_eng[i][0])

                    elif (words_tags_eng[i][0]=="NN"):
                        #append corresponding Hindi NP
                        j = get_phrase_pos(heads_eng,i,heads_hin)
                        if(j==-1):
                            append_eng=True
                        else:
                            code_mixed_sent.append(heads_hin[j])
                
                        """j = get_phrase_pos(heads_eng,i,heads_hin)
                        if(j==-1):
                            append_eng=True
                        else:
                            for word in phrases_hin[j]:
                                code_mixed_sent.append(word)"""
                    
                        


                    elif words_tags_eng[i][0]=="NNP" or words_tags_eng[i][0]=="NNS":
                        #append the head of corresponding NP
                        j = get_phrase_pos(heads_eng,i,heads_hin)
                        if(j==-1):
                            append_eng=True
                        else:
                            code_mixed_sent.append(heads_hin[j])
                    else:
                        j = get_phrase_pos(heads_eng,i,heads_hin)
                        if(j==-1):
                            append_eng=True
                        else:
                            code_mixed_sent.append(heads_hin[j])

                if (s==2):
                    if words_tags_eng[i][0]=="VBG" and (words_tags_eng[i][1]=="NNS" or words_tags_eng[i][1]=="NN"):
                        #append corresponding NP 
                        j = get_phrase_pos(heads_eng,i,heads_hin)
                        if(j==-1):
                            append_eng=True
                        else:
                            for word in phrases_hin[j]:
                                code_mixed_sent.append(word)
                                
                    elif words_tags_eng[i][0]=="JJ" and (words_tags_eng[i][1]=="NNS" or words_tags_eng[i][1]=="NN"):
                        #append corresponding NP "without PSP"
                        j = get_phrase_pos(heads_eng,i,heads_hin)
                        if(j==-1):
                            append_eng=True
                        else:
                            for word in phrases_hin[j]:
                                code_mixed_sent.append(word)

                    elif (words_tags_eng[i][0]=="PRP" or words_tags_eng[i][0]=="PRP$") and (words_tags_eng[i][1]=="NNS" or words_tags_eng[i][1]=="NN"):
                        #append corresponding NP
                        j = get_phrase_pos(heads_eng,i,heads_hin)
                        if(j==-1):
                            append_eng=True
                        else:
                            for word in phrases_hin[j]:
                                code_mixed_sent.append(word)
                        if(s>2 and append_eng==False):
                            code_mixed_sent.append(phrases_eng[i][2])

                    elif words_tags_eng[i][0]=="DT" and (words_tags_eng[i][1]=="NNS" or words_tags_eng[i][1]=="NN"):
                        code_mixed_sent.append(phrases_eng[i][0])
                        #append head of corresponding Hindi NP
                        j = get_phrase_pos(heads_eng,i,heads_hin)
                        if(j==-1):
                            append_eng=True
                        else:
                            code_mixed_sent.append(heads_hin[j])
                        if(s>2 and append_eng==False):
                            code_mixed_sent.append(phrases_eng[i][2])

                    elif words_tags_eng[i][0]=="NN" and words_tags_eng[i][1]=="POS":
                        #append corresponding NP
                        j = get_phrase_pos(heads_eng,i,heads_hin)
                        if(j==-1):
                            append_eng=True
                        else:
                            for word in phrases_hin[j]:
                                code_mixed_sent.append(word)
                    elif words_tags_eng[i][0]=="NNP" and words_tags_eng[i][1]=="RB":
                        j = get_phrase_pos(heads_eng,i,heads_hin)
                        if(j==-1):
                            append_eng=True
                        else:
                            for word in phrases_hin[j]:
                                code_mixed_sent.append(word)
                    else:
                        for x in range(len(words_tags_eng[i])):
                            if words_tags_eng[i][x]!="NN" and words_tags_eng[i][x]!="NNS":
                                code_mixed_sent.append(phrases_eng[i][x])
                            else:
                                j = get_translation(phrases_eng[i][x],heads_hin)
                                if(j==-1):
                                    code_mixed_sent.append(phrases_eng[i][x])
                                else:
                                    code_mixed_sent.append(heads_hin[j])
                        """"if(words_tags_eng[i][s-1]=="NN" or words_tags_eng[i][s-1]=="NNS"):
                            for k in range(s-1):
                                code_mixed_sent.append(phrases_eng[i][k])
                            #append head of corresponding Hindi NP
                            j = get_phrase_pos(heads_eng,i,heads_hin)
                            if(j==-1):
                                append_eng=True
                            else:
                                code_mixed_sent.append(heads_hin[j])"""

                if(s==3):
                    if words_tags_eng[i][0]=="DT" and words_tags_eng[i][1]=="JJ" and (words_tags_eng[i][2]=="NN" or words_tags_eng[i][2]=="NNS"):
                        #append corresponding NP
                        j = get_phrase_pos(heads_eng,i,heads_hin)
                        if(j==-1):
                            append_eng=True
                        else:
                            for word in phrases_hin[j]:
                                code_mixed_sent.append(word)

                    elif words_tags_eng[i][0]=="RB" and words_tags_eng[i][1]=="DT" and (words_tags_eng[i][2]=="NN" or words_tags_eng[i][2]=="NNS"):
                        #append corresponding NP or its head
                        j = get_phrase_pos(heads_eng,i,heads_hin)
                        if(j==-1):
                            append_eng=True
                        else:
                            code_mixed_sent.append(heads_hin[j])
                    elif words_tags_eng[i][0]=="DT" and words_tags_eng[i][2]=="WDT" and (words_tags_eng[i][1]=="NN" or words_tags_eng[i][1]=="NNS"):
                        j = get_phrase_pos(heads_eng,i,heads_hin)
                        if(j==-1):
                            append_eng=True
                        else:
                            for word in phrases_hin[j]:
                                code_mixed_sent.append(word)
                            code_mixed_sent.append(phrases_eng[i][2])
                            
                        
                    else:
                        for x in range(len(words_tags_eng[i])):
                            if words_tags_eng[i][x]!="NN" and words_tags_eng[i][x]!="NNS":
                                code_mixed_sent.append(phrases_eng[i][x])
                            else:
                                j = get_translation(phrases_eng[i][x],heads_hin)
                                if(j==-1):
                                    code_mixed_sent.append(phrases_eng[i][x])
                                else:
                                    code_mixed_sent.append(heads_hin[j])
                        """"if(words_tags_eng[i][s-1]=="NN" or words_tags_eng[i][s-1]=="NNS"):
                            for k in range(s-1):
                                code_mixed_sent.append(phrases_eng[i][k])
                            #append head of corresponding Hindi NP
                            j = get_phrase_pos(heads_eng,i,heads_hin)
                            if(j==-1):
                                append_eng=True
                            else:
                                code_mixed_sent.append(heads_hin[j])"""
                if(s>3):
                    for x in range(len(words_tags_eng[i])):
                        if words_tags_eng[i][x]!="NN" and words_tags_eng[i][x]!="NNS":
                            code_mixed_sent.append(phrases_eng[i][x])
                        else:
                            j = get_translation(phrases_eng[i][x],heads_hin)
                            if(j==-1):
                                code_mixed_sent.append(phrases_eng[i][x])
                            else:
                                code_mixed_sent.append(heads_hin[j])



            else:
                for word in phrases_eng[i]:
                    code_mixed_sent.append(word)
                    
            if(append_eng):
                for word in phrases_eng[i]:
                    code_mixed_sent.append(word)
    for words in code_mixed_sent:
        mixed_file.write(words)
        mixed_file.write(" ")
    mixed_file.write("\n")
    code_mixed_sent=[]
mixed_file.close()


