from nltk.book import * #import the texts

#Q24
sorted(w for w in set(text6) if w.endswith('ise')) #sort a list of words ending with 'ise'
sorted(w for w in set(text6) if 'z' in w) #sort a list of words containing a letter 'z'
sorted(w for w in set(text6) if 'pt' in w) #sort a list of words containing a sequence of 'pt'
sorted(w for w in set(text6) if w.istitle()) #sort a list of words having initial capticals




#Q25
sent = ["she", "sells", "sea", "shells", "by", "sea", "the", "shore"] #create a list called 'sent'
sent1 = [w for w in set(sent) if w.startswith('sh')] #define a list that contains the words starting with 'sh' and named it as sent1
print(sent1) #output the list called sent1
sent2 = [w for w in set(sent) if len(w)>4] #defining a list that contains words longer than 4 characters
print(sent2) #output the list called sent2
