from nltk.corpus import gutenberg

for fileid in gutenberg.fileids():
    num_chars=len(gutenberg.raw(fileid))
    num_words=len(gutenberg.words(fileid))
    num_sents=len(gutenberg.words(fileid))
    num_vocab=len(set([w.lower() for w in gutenberg.words(fileid)]))
    print num_chars,num_words,num_sents,num_vocab,int(num_chars/num_words),int(num_words/num_sents),int(num_words/num_vocab),fileid

