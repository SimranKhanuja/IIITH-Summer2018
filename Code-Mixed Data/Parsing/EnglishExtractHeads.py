from nltk.tree import ParentedTree
eng=open('ParsedLowEngWPOSingle.txt',encoding='utf-8')
content = eng.read().split("\n")
allsent = []
allpos = []
list_of_phrase_tags=['VP','NP','ADJP','ADVP']
heads = {"NP":["NNS","NNP",'PRP','NN','NNPS'],
             "VP":['VBP','VBZ','VBG','VBD','VBN','VB'],
             "ADJP":['JJR','JJS','JJ','VBN'],
             "ADVP":['RB','RBR'],
             "CC" : ['CC'],
             "IN" : ['IN']}
for q in content:
    ptree = ParentedTree.fromstring(q)
    leaf_values = ptree.leaves()
    #ptree.pretty_print()
    ls = []
    pos={}
    for x in ptree.leaves():
        i = -2
        leaf_index = leaf_values.index(x)
        tree_location = ptree.leaf_treeposition(leaf_index)
        y=str(ptree[tree_location[:i]])
        p=str(ptree[tree_location[:-1]])
        indexp = p.find(" ")
        indexnp = p.find("\n")
        if(indexnp<indexp and indexnp!=(-1)):
            indexp = indexnp
        pos.update({x:p[1:indexp]})
        while(i>-(ptree.height())):
            indexy = y.find(" ")
            indexny = y.find("\n")
            if(indexny<indexy and indexny!=(-1)):
                indexy = indexny
            if(y[1:indexy] in list_of_phrase_tags):
                ls.append([x, y[1:indexy]])
                break
            else:
                i=i-1
                y=str(ptree[tree_location[:i]])
    tag = ls[0][1]
    chunk=[]
    st = []
    i=0
    for x in ls:
        y = x[0]
        if(pos.get(y)=='CC'):
                chunk.append([tag,st])
                st=[]
                st.append(y)
                tag="CC"
        elif(pos.get(y)=='IN'):
                chunk.append([tag,st])
                st=[]
                st.append(y)
                tag="IN"
        elif x[1]==tag:
            st.append(y)
        else:
            if x[1]=='PP' and pos.get(y) not in ('IN'):
                st.append(y)
                x[1]=tag
            elif x[1]=='ADVP' and (tag=='NP' or tag =='VP'):
                st.append(y)
                x[1]=tag
            else:    
                chunk.append([tag,st])
                tag = x[1]
                st =[]
                st.append(y)
    chunk.append([tag,st])
    for x in chunk:
        for y in heads.keys():
            if x[0]==y:
                l = heads.get(y)
                for z in x[1]:
                    if pos.get(z) in l:
                        x[1].append(z)
                        break
    allsent.append(chunk)
    allpos.append(pos)
