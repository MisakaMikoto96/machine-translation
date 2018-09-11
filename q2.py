from nmt_config22 import *
from nltk import FreqDist
import matplotlib.pyplot as plt
from nltk import tokenize
from nltk.tokenize import WordPunctTokenizer
print(vocab_path)
import matplotlib
from nltk import tokenize
import re
# 1.Plot (choose sensible graphs) the distribution of sentence lengths
# in the English and Japanese and their correlation. What do you infer
# from this about translating between these languages?


with open(text_fname['en']) as e:
    tokenlist_en=[]
    sent_len_en=[]
    for lines in e:
        lines=lines.replace(' &apos;', '')
        lines=lines.replace(' &quot;','')
        lines=lines.replace('@-@', '')
        a = WordPunctTokenizer().tokenize(lines)
        sent_len_en.append(len(a))
        number_of_tokens_en = sum(sent_len_en)
        for words in a:
            tokenlist_en.append(words)
    print('token',tokenlist_en)
    print('number of tokens', number_of_tokens_en)

word_type_en = (sorted(set(tokenlist_en)))
print (word_type_en)
len_of_word_type_en=len(word_type_en)
print ('word type of English:',len_of_word_type_en)
print ('length of en_sents',sent_len_en)



with open(text_fname['fr']) as j:
    tokenlist_jp=[]
    sent_len_jp=[]
    for lines1 in j:
        b=WordPunctTokenizer().tokenize(lines1)
        sent_len_jp.append(len(b))
        numbere_of_tokens_jp=sum(sent_len_jp)
        for words in b:
            tokenlist_jp.append(words)
    print ('number of tokens',len(tokenlist_jp))

word_type_jp = (sorted(set(tokenlist_jp)))
len_of_word_type_jp=len(word_type_jp)
print('word type of Japanese:', len_of_word_type_jp)
print ('length of jp_sents',sent_len_jp)



#===========================
#graph

x= (sorted(sent_len_en))
print ('x',x)
y= (sorted(sent_len_jp))
print ('y',y)

label = ["English", "Japanese"]
plt.hist(x,bins= 500,color='r',label='English')
en=plt.hist(sent_len_jp,bins = 500,color='g',label = 'Japanese')
jp=plt.title('Length of Sentence in English Japanese')
plt.legend(label,loc=0,ncol=2)
plt.show()

plt.scatter(sent_len_en,sent_len_jp,s=20,marker='.')
plt.title('Correlation')
plt.show()


#====================================================
print('ty/to-en',len(word_type_en)/len(tokenlist_en))
print('ty/to-jp',len(word_type_jp)/len(tokenlist_jp))

#==========================
#_UNK_
def len_of_UNK_WORD(token):
    unique=[]
    for unique_word in list(token):
        if token.count(unique_word)==1:
            unique.append(unique_word)

    return len(unique)



c=len_of_UNK_WORD(tokenlist_en)
print('_UNK_ in English',c)
d=len_of_UNK_WORD(tokenlist_jp)
print('_UNK_ in Japanede',d)


