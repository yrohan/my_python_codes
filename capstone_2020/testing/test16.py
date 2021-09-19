from pycorenlp import StanfordCoreNLP

text_amb = "everything tastes like garbage to me but we keep coming back because my wife loves the pasta"

nlp = StanfordCoreNLP('http://localhost:9000')


def get_sentiment(text):
    res = nlp.annotate(text,
                       properties={'annotators': 'sentiment',
                                   'outputFormat': 'json',
                                   'timeout': 1000,
                                   })
    print(text)
    print('Sentiment:', res['sentences'][0]['sentiment'])
    print('Sentiment score:', res['sentences'][0]['sentimentValue'])
    print('Sentiment distribution (0-v. negative, 5-v. positive:', res['sentences'][0]['sentimentDistribution'])


get_sentiment(text_amb)
