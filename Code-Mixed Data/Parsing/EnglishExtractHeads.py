from nltk.tree import ParentedTree
ptree = ParentedTree.fromstring("(ROOT (S (NP (PRP You)) (VP (VBP keep) (NP (PRP yourself)) (ADVP (RB far) (PP (IN from) (NP (JJ many) (NNS diseases)))) (PP (IN by) (S (VP (VBG eating) (NP (ADJP (RBR less) (JJ fatty) (CC and) (JJ fatty)) (NN food)))))) (. .)))")
leaf_values = ptree.leaves()
ptree.pretty_print()
ls = []
list_of_phrase_tags=['VP','NP','ADJP','ADVP']
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
            ls.append({x : y[1:indexy]})
            break
        else:
            i=i-1
            y=str(ptree[tree_location[:i]])
heads = {"NP":["NNS","NNP",'PRP'],
         "VP":['VBP','VBZ','VBG'],
         "ADJP":['JJ'],
         "ADVP":['RB','RBR'],
         "CC" : ['CC']}
tag = list(ls[0].values())[0]
chunk=[]
st = []
i=0
for x in ls:
    y = list(x.keys())[0]
    if list(x.values())[0]==tag:
        if(pos.get(y)=='CC'):
            chunk.append({tag:st})
            st=[]
            st.append(y)
            chunk.append({"CC":st})
            st=[]
        else:
            st.append(y)
    else:
        chunk.append({tag:st})
        tag = list(x.values())[0]
        st =[]
        st.append(y)
chunk.append({tag:st})
for x in chunk:
    for y in heads.keys():
        if list(x.keys())[0]==y:
            l = heads.get(y)
            for z in list(x.values())[0]:
                if pos.get(z) in l:
                    z = "*" + z + "*"
                    list(x.values())[0].append("head:"+z)
                    break
print(chunk)
        
    
        
