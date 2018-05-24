from xml.dom import minidom
from nltk import word_tokenize
import re
mydoc = minidom.parse(r'C:\Users\Simran Khanuja\.atom\packages\script\smsCorpus_en_2014.09.06_all.xml')#importing xml file data
toparse = mydoc.getElementsByTagName('text')#make objects of "text" tag
for elem in toparse:
    x = elem.firstChild.data.encode('ascii', 'ignore').decode()# get data stored in text tag
    print(re.findall(r'https?://[\.\w]+|[\w\._%+-]+@[\w\.-]+\.\w+|[A-Z][a-z]+(?=[A-Z])|[\'\w\-\$]+|[\,\.\!\@\#\&\*\/\:]+',x))# tokenization of the data
    #https?://[\.\w]+ == parsing for urls
    #[\w\._%+-]+@[\w\.-]+\.\w+ == parsing for email addresses
    #[\'\w\-\$]+ == any word with special characters preserved
    #[A-Z][a-z]+(?=[A-Z]) == parses words like AvailableOnly
    #[\,\.\!\@\#\&\*\/\:]+ == recognizes special character as tokens as well
    
