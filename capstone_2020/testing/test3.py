from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from nltk import sent_tokenize, word_tokenize, pos_tag

lemmatizer=WordNetLemmatizer()

def penn_to_wn(tag):
    '''
    Convert between penn treebank tags to Simple wordnet Tags
    '''
    if tag.startswith('J'):
        return wn.ADJ
    elif tag.startswith('N'):
        return wn.NOUN
    elif tag.startswith('R'):
        return wn.ADV
    elif tag.startswith('V'):
        return wn.VERB
    return None

def clean_text(text):
    text=text.replace("<br />"," ")
    text=text.decode("utf-8")

    return text

def swn_polarity(text):
    '''
    Return a sentiment polarity 0:negative 1:positive
    '''

    sentiment=0.0
    tokens_count=0

    text=clean_text(text)

    raw_sentences=sent_tokenize(text)
    for raw_sentence in raw_sentences:
        tagged_sentence=pos_tag(word_tokenize(raw_sentence))

        for word, tag in tagged_sentence:
            wn_tag=penn_to_wn(tag)
            if wn_tag not in (wn.NOUN, wn.ADJ, wn.ADV):
                continue

            lemma=lemmatizer.lemmatize(word,pos=wn_tag)
            if not lemma:
                continue

            synsets=wn.synsets(lemma, pos=wn_tag)
            if not synsets:
                continue

            synset=synsets[0]
            swn_synset=swn.senti_synset(synset.name())

            sentiment =sentiment + swn_synset.pos_score()-swn_synset.neg_score()
            tokens_count=tokens_count+1

            if not tokens_count:
                return 0

            if sentiment>=0:
                return 1

            return 0

