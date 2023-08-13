import os
from dotenv import load_dotenv
import tweepy

class ImageTweet:

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('CONSUMER_KEY')
        self.api_secret = os.getenv('CONSUMER_SECRET')
        self.access_token = os.getenv('ACCESS_TOKEN')
        self.access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

    def get_twitter_conn_v1(self) -> tweepy.API:
        auth = tweepy.OAuth1UserHandler(self.api_key, self.api_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        return tweepy.API(auth)

    def get_twitter_conn_v2(self) -> tweepy.Client:
        client = tweepy.Client(
            consumer_key=self.api_key,
            consumer_secret=self.api_secret,
            access_token=self.access_token,
            access_token_secret=self.access_token_secret,
        )
        return client

    def tweet(self, media_path):
        client_v1 = self.get_twitter_conn_v1()
        client_v2 = self.get_twitter_conn_v2()

        media = client_v1.media_upload(filename=media_path)
        status = "【Oshi no Ko】 " + media_path.split("_")[0]
        media_id = media.media_id

        client_v2.create_tweet(text=status, media_ids=[media_id])
