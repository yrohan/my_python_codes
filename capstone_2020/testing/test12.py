import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer

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
my_sent = usr_comment.lower()
my_words = [word for word in word_tokenize(my_sent) if not word in all_stopwords]
my_stems = []
for i in range(0,len(my_words)):
    my_stems.append(ps.stem(my_words[i]))
print("\n",my_stems)
for word in my_words:
    if word in senti_words:
        score = score + senti_word_scores.get(word)

print("\n")
print("Final Score = ", score)

print("\n")
print(usr_review)
score = 0
my_sent = usr_review.lower()
my_words = [word for word in word_tokenize(my_sent) if not word in all_stopwords]
for word in my_words:
    if word in senti_words:
        score = score + senti_word_scores.get(word)

print("\n")
print("Final Score = ", score)