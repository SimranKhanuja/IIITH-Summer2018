Descriptions of Tasks
 
Task 1 : Tokenization is the process of identification of tokens. Example: 'On Tuesday, however, the pacers found their calling.', can be tokenized as 'On Tuesday , however , the pacers found their calling .', where ',' and '.' are identified as tokens along with the words. SMS data is always hard to tokenize as people tend to write words without giving spaces. The dataset given for this task is an xml file. First task is to extract the message, and then tokenize. Create your own tokenizer, creating tokenization requires identification of patterns which can be achieved through regular expressions. See where you are finding trouble. Use custom tokenizers available in nltk, if you have not installed install this package (python nltk package) as the next task.

Task 2 : After the tokenization in problem 1, find out the unigram, bigram and trigram frequencies and their probabilities of the words apearing in the messages. If you have not read about n-grams, read the Jurafsky book. Bigram and trigram probabilities can be calculated either by joint or conditional probabilities.

