import time
import requests

from image_upload import ImageTweet
from video_upload import VideoTweet
from utilities import *

from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/health')
def health():
    tweet()
    return '200 OK'


def tweet():

    file = getRandomFile()

    if file['extension'] == 'mp4':
        videoTweet = VideoTweet(file['title'])
        videoTweet.tweet()

    if file['extension'] == 'png':
        imageTweet = ImageTweet(file['title'])
        imageTweet.tweet()

def ping():

    try:
        r = requests.head("https://oshi.onrender.com")
        print(r.status_code)

    except requests.ConnectionError:
        print("failed to connect")

if __name__ == '__main__':
    app.run()
