from nltk.corpus import PlaintextCorpusReader

corpus_root='C:/Users/Linux/Documents/dict'

wordlists=PlaintextCorpusReader(corpus_root,'.*')

print(wordlists)

print(wordlists.fileids())

print("done")

