from xml.dom import minidom
from nltk import word_tokenize
import re
mydoc = minidom.parse(r'C:\Users\Simran Khanuja\.atom\packages\script\smsCorpus_en_2014.09.06_all.xml')
toparse = mydoc.getElementsByTagName('text')
for elem in toparse:
    x = elem.firstChild.data
    print(re.findall(r"[A-Z][a-z]+(?=[A-Z])|[\'\w\-\$]+|[\,\.\!\@\#\&\*]+",x))
    #[A-Z][a-z]+(?=[A-Z] == AvailableOnly)
    #[\'\w\-\$]+ == any word with - ' and $ preserved
    # recognizes special characters as tokens as WeLL
