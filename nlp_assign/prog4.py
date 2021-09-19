from nltk import FreqDist
from nltk.corpus import state_union

fname=state_union.fileids()
cur_year=[]
count_word=[]
occur_words=['men','women','people']
length1=len(fname)
length2=len(occur_words)
for i in range(0,length1):
fdist=FreqDist(fname[0])
count_word.append(fdist[occur_words[0]])

print count_word