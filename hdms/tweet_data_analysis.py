import pandas as pd

tweet_sample_data = pd.read_csv("C:/Users/Linux/PycharmProjects/hdms/datasets/twcs.csv")
row, column = tweet_sample_data.shape
col_names = list(tweet_sample_data.columns)
print(col_names)
auth_id = list(tweet_sample_data[col_names[1]])
unique_auth_id = list(tweet_sample_data[col_names[1]].unique())
no_of_tweets = []
for i in range(len(unique_auth_id)):
    no_of_tweets.append(auth_id.count(unique_auth_id[i]))
print("{0:<15}".format("Author ID") + "    Number of Tweets")
for i in range(len(unique_auth_id)):
    print("{0:<15}".format(unique_auth_id[i]), " :  ", no_of_tweets[i])

first_inbound = tweet_sample_data[pd.isnull(tweet_sample_data.in_response_to_tweet_id) & tweet_sample_data.inbound]
print('Found {} first inbound messages.'.format(len(first_inbound)))

# Merge in all tweets in response
inbounds_and_outbounds = pd.merge(first_inbound, tweet_sample_data, left_on='tweet_id',
                                  right_on='in_response_to_tweet_id')
print("Found {} responses.".format(len(inbounds_and_outbounds)))

# Filter out cases where reply tweet isn't from company
inbounds_and_outbounds = inbounds_and_outbounds[inbounds_and_outbounds.inbound_y ^ True]
print("Found {} responses from companies.".format(len(inbounds_and_outbounds)))
print("\nsuccess")