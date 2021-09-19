from nltk.corpus import brown

count=0
words=brown.words()
low_words=[w.lower() for w in set(words)]
for w1 in low_words:
    if w1.startswith('wh'):
        count=count+1;


print count