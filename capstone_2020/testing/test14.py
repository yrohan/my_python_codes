import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

all_stopwords = stopwords.words('english')
ps = SnowballStemmer("english")
senti_words = ["good","bad","average","masterpiece","absolute","best","brilliant","massive","achievement"]
senti_word_scores={"good":6, "best":8, "brilliant":9, "average":5, "bad":3, "masterpiece":9, "absolute":1, "massive":5, "achievement":3}
acting_words = ["acting","performance"]
acting_word_scores = {}
plot_words = ["writing","scene"]
plot_word_scores = {}
db_file1 = pd.read_csv("C:/Users/Linux/PycharmProjects/capstone_2020/movie_reviews.csv")
usr_comment = db_file1["Comment"][0]
usr_review = db_file1["Reviews"][0]
print(usr_comment)
score = 0
my_sent1 = usr_comment.lower()
my_words1 = sent_tokenize(my_sent1)
print("\n")
print(usr_review)
my_sent2 = usr_review.lower()
my_words2 = sent_tokenize(my_sent2)
sid = SentimentIntensityAnalyzer()
for sents in my_words1:
    print(sents, "\n")
    ss = sid.polarity_scores(sents)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print()
print("\n\n")
for sents in my_words2:
    print(sents,"\n")
    ss = sid.polarity_scores(sents)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print()

print("\n")
print("Final Score = ", score)