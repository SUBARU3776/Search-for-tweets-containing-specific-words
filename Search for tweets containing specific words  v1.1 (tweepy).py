import tweepy

# Twitter APIの認証情報
consumer_key = 'tZxS08taz6eqPJHsPkt5bsD19'
consumer_secret = 'zIGuCCxRmeJ7UMiRErHIPimIq6MnF3BXybK69LEX3KaCGPourz'
access_token = '269515119-of2MGRqJQYOUpB12JtJUEJhrqcZ76uaB5iCXHgXy'
access_token_secret = 'pzhfaSDYNWe47nTVajskGrth1Zcwr9kuZCphOOesHk2k5'

# 認証情報を使用して Twitter APIにアクセス
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# 特定のキーワードを含む最新の10件のツイートを検索
all_tweets = []
query = "これから大切なことを言います。"
search_results = api.search_tweets(q=query, count=10)
for tweet in search_results:
    all_tweets.append(tweet.text)

# 検索結果を表示
for tweet in all_tweets:
    print(tweet)