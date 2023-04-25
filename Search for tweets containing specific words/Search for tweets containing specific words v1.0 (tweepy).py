import tweepy
#Twitter APIの認証情報
consumer_key= 'Your_consumer_key'
consumer_secret = 'Your_consumer_secret'
access_token = 'Your_access_token' 
access_token_secret = 'Your_access_token_secret'

# 認証情報を使用して Twitter APIにアクセス
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy. API(auth)

#特定のキーワードを含む最新の10件のツイートを検索
search_query="これから大切なことを言います。"
search_results = api.search_tweets(q=search_query, count=10)

# 検索結果を表示
for tweet in all_tweets:
    print(tweet)
    
