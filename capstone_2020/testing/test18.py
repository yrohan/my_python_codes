from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import re

all_stopwords = stopwords.words('english')
analyzer = SentimentIntensityAnalyzer()
good_word = ["phenomenal","moved"]
bad_word = ["garbage"]


def sentiment_analyzer_scores(text):
    score = analyzer.polarity_scores(text)
    compound_score = score['compound']
    all_word = word_tokenize(text)
    for i in range(0,len(all_word)):
        if all_word[i] in good_word:
            compound_score += 0.7
        if all_word[i] in bad_word:
            compound_score += -0.7

    return compound_score


plot_words = ["writing", "scene", "cinematography", "plot", "script", "scenography"]
acting_words = ["acting", "performance", "directing", "role", "performances"]
sound_words = ["song", "sound"]
found_plot_words = []
found_acting_words = []
found_sound_words = []
all_relevant_comm_words = []
all_relevant_revw_words = []
tot_acting_score = 0
tot_plot_score = 0
tot_sound_score = 0
tot_comment_score = 0
tot_review_score = 0
review_data = pd.read_csv("C:/Users/Linux/PycharmProjects/capstone_2020/movie_reviews.csv")
row, column = review_data.shape
for i in range(0, row):
    usr_comment = review_data["Comment"][i]
    usr_review = review_data["Reviews"][i]
    tot_comment_score = tot_comment_score + (sentiment_analyzer_scores(usr_comment) * int(review_data["UsrRating"][i]))
    tot_review_score = tot_review_score + (sentiment_analyzer_scores(usr_review) * int(review_data["UsrRating"][i]))
    comment_sent = sent_tokenize(usr_comment)
    rev_sent = sent_tokenize(usr_review)
    for sent in comment_sent:
        comment_words = word_tokenize(sent)
        for i in range(0, len(comment_words)):
            comment_word = comment_words[i].lower()
            if comment_word in acting_words:
                found_acting_words.append(comment_word)
                tot_acting_score += sentiment_analyzer_scores(sent)
            if comment_word in plot_words:
                found_plot_words.append(comment_word)
                tot_plot_score += sentiment_analyzer_scores(sent)
            if comment_word in sound_words:
                found_sound_words.append(comment_word)
                tot_sound_score += sentiment_analyzer_scores(sent)
    for sent in rev_sent:
        rev_words = word_tokenize(sent)
        for i in range(0, len(rev_words)):
            rev_word = rev_words[i].lower()
            if rev_word in acting_words:
                found_acting_words.append(rev_word)
                tot_acting_score += sentiment_analyzer_scores(sent)
            if rev_word in plot_words:
                found_plot_words.append(rev_word)
                tot_plot_score += sentiment_analyzer_scores(sent)
            if rev_word in sound_words:
                found_sound_words.append(rev_word)
                tot_sound_score += sentiment_analyzer_scores(sent)
    del comment_words
    del rev_words

for i in range(0, row):
    usr_comment = review_data["Comment"][i]
    usr_review = review_data["Reviews"][i]
    comm_words = word_tokenize(usr_comment.lower())
    revw_words = word_tokenize(usr_review.lower())
    for i in range(0, len(comm_words)):
        if comm_words[i] not in all_stopwords:
            all_relevant_comm_words.append(comm_words[i])
    for i in range(0, len(revw_words)):
        if revw_words[i] not in all_stopwords:
            all_relevant_revw_words.append(revw_words[i])

all_relevant_comm_words = list(set(all_relevant_comm_words))
all_relevant_revw_words = list(set(all_relevant_revw_words))
all_relevant_comm_words = [re.sub('\?|\'|!+|[0-9]+|#|>|=|\(|\)|\:', '', item) for item in all_relevant_comm_words]
all_relevant_revw_words = [re.sub('\?|\'|!+|[0-9]+|#|>|=|\(|\)|\:', '', item) for item in all_relevant_revw_words]
all_relevant_comm_words = [re.sub('[./-]', ' ', item) for item in all_relevant_comm_words]
all_relevant_revw_words = [re.sub('[./-]', ' ', item) for item in all_relevant_revw_words]

while ('' in all_relevant_comm_words):
    all_relevant_comm_words.remove('')
while (' ' in all_relevant_comm_words):
    all_relevant_comm_words.remove(' ')
while ('   ' in all_relevant_comm_words):
    all_relevant_comm_words.remove('   ')
while ('' in all_relevant_revw_words):
    all_relevant_revw_words.remove('')
while (' ' in all_relevant_revw_words):
    all_relevant_revw_words.remove(' ')

tot_acting_score = round((tot_acting_score/len(found_acting_words)*10), 1)
tot_plot_score = round((tot_plot_score/len(found_plot_words)*10), 1)
tot_sound_score = round((tot_sound_score/len(found_sound_words)*10), 1)
tot_comment_score = round((tot_comment_score / len(all_relevant_comm_words)*10), 1)
tot_review_score = round((tot_review_score / len(all_relevant_revw_words)*10), 1)
found_acting_words = list(set(found_acting_words))
found_plot_words = list(set(found_plot_words))
found_sound_words = list(set(found_sound_words))
if tot_acting_score > 10:
    tot_acting_score = 10
if tot_plot_score > 10:
    tot_plot_score = 10
if tot_sound_score > 10:
    tot_sound_score = 10
if tot_comment_score > 10:
    tot_comment_score = 10
if tot_review_score > 10:
    tot_review_score = 10
print("\n Total Comment score is ", tot_comment_score)
print("\n Total Review Score is ", tot_review_score)
print("\n Total Acting score is ", tot_acting_score)
print("\n Total Plot Score is ", tot_plot_score)
print("\n Total Sound score is ", tot_sound_score)
'''print("\n Found Acting Words\n", found_acting_words)
print("\n Found Plot Words\n", found_plot_words)
print("\n Found Sound Words\n", found_sound_words)
print("\n Relevant Comment words found are ", all_relevant_comm_words)
print("\n Relevant Review Words found are ", all_relevant_revw_words)'''
