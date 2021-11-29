# excercise 18
import nltk
import re
from nltk.corpus import * 
from nltk.corpus import gutenberg
from nltk.corpus import stopwords

words_list = []  #create an empty list
#define a function
def bigrams50(text):  
    text0 = [w for w in text if w.isalpha()]
    stop_words = nltk.corpus.stopwords.words('english')
    for w in text0:
        if w.lower() in stop_words:
            w = "SW"
        words_list.append(w)

    bigrams_list = []
    for w in range(len(words_list)-1): #list index out of range
        bigram = (words_list[w], words_list[w+1]) #list indices must be integers or slices, not str
        if "SW" not in bigram:
            bigrams_list.append(bigram) 
   
    fd = nltk.FreqDist(bigrams_list)
    print(fd.most_common(50))

text1 = gutenberg.words('austen-emma.txt') #call function 
bigrams50(text1)







# excercise 19
import nltk
from nltk.corpus import brown  #import brown corpus

genres = brown.categories()  #import genres in brown corpus

cfd = nltk.ConditionalFreqDist(
    (genre, word) 
    for genre in genres 
    for word in brown.words(categories=genre))  #check conditional frequency distributions by genre

time = ['morning', 'night', 'day', 'afternoon', 'evening']  #create the list of event words

cfd.tabulate(conditions=genres, samples=time)  #create a table of distributions of event words by genre 
