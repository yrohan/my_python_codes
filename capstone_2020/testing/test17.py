from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

analyzer = SentimentIntensityAnalyzer()


def sentiment_analyzer_scores(text):
    score = analyzer.polarity_scores(text)
    return score['compound']


tot_comment_score = 0
tot_review_score = 0
review_data = pd.read_csv("C:/Users/Linux/PycharmProjects/capstone_2020/movie_reviews.csv")
row,column = review_data.shape
for i in range(0,row):
    usr_comment = review_data["Comment"][i]
    usr_review = review_data["Reviews"][i]
    tot_comment_score = tot_comment_score + (sentiment_analyzer_scores(usr_comment)*int(review_data["UsrRating"][i]))
    tot_review_score = tot_review_score + (sentiment_analyzer_scores(usr_review)*int(review_data["UsrRating"][i]))

tot_comment_score = round((tot_comment_score/10),1)
tot_review_score = round((tot_review_score/10),1)
if tot_comment_score > 10:
    tot_comment_score = 10
if tot_review_score > 10:
    tot_review_score = 10
print("\n Total Comment score is ", tot_comment_score)
print("\n Total Review Score is ", tot_review_score)