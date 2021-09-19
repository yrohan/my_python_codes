from nltk import FreqDist
from nltk.corpus import brown

words=brown.words()
fdist=FreqDist([w.lower() for w in words])
modals=['can','could','may','might','must','will']
for m in modals:
    print m+':',fdist[m]

