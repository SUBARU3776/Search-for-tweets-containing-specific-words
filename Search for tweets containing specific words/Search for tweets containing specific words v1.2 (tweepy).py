# 認証情報を設定
consumer_key= 'Your_consumer_key'
consumer_secret = 'Your_consumer_secret'
access_token = 'Your_access_token' 
access_token_secret = 'Your_access_token_secret'

# OAuth認証を処理するための設定
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Twitter APIを使用するためのインスタンスを作成
api = tweepy.API(auth)

# ワードサーチを実行
all_tweets = []
query = '@_SUBARU_3776_'

# 1000件で抽出はストップ
max_tweets = 1000
while len(all_tweets) < max_tweets:
    tweets = api.search_tweets(q=query, 
                        count=200,
                        lang='ja',
                        tweet_mode='extended',
                        max_id=all_tweets[-1].id - 1 if all_tweets else None
                       )
    if not tweets:
        break
    all_tweets.extend(tweets[:min(max_tweets - len(all_tweets), 100)])
    time.sleep(1) # 1秒間のアイドリングを挟む
    
# ツイートの情報を取得してデータフレームに追加
data = pd.DataFrame(data=[[tweet.id, tweet.created_at.astimezone(timezone(timedelta(hours=+9))), tweet.user.id, tweet.user.name, tweet.full_text.replace('\n', ' '), tweet.retweeted_status.id_str if hasattr(tweet, 'retweeted_status') else None] for tweet in all_tweets], columns=['tweet_id', 'created_at', 'user_id', 'user_name', 'tweet_text', 'retweeted_id'])


# CSVファイルとして保存(タイムスタンプ付き)
now = datetime.now()
timestamp = now.strftime("%Y%m%d%H%M%S")
file_name = f"tweepy_{query}_{timestamp}.csv"
data.to_csv(file_name, index=False)

# 保存されたファイルの5行を表示
saved_data = pd.read_csv(file_name)
print(saved_data.head())
print(f"Tweets saved to file: {file_name}")
