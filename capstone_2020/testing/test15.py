from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def sentiment_analyzer_scores(text):
    score = analyzer.polarity_scores(text)
    print(text)
    print(score)


text_pos = 'this place was amazing  great food and atmosphere'
sentiment_analyzer_scores(text_pos)
text_neg = 'i didnt like their italian sub though just seemed like lower quality meats on it and american cheese'
sentiment_analyzer_scores(text_neg)
text_amb = "everything tastes like garbage to me but we keep coming back because my wife loves the pasta"
sentiment_analyzer_scores(text_amb)
