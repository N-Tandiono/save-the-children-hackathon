from flask import Flask, render_template, request
import requests
import tweepy
from textblob import TextBlob
from tokens import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_SECRET_TOKEN

APP = Flask(__name__)

@APP.route('/')
def index():
    return render_template('index.html')

@APP.route('/feed')
def feed():
    text = request.args.get('search')

    feeds = []

    if text:
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)

        api = tweepy.API(auth)
        public_tweets = api.search(text)
        
        for tweet in public_tweets:
            analysis = TextBlob(tweet.text)
            # data.append({'text': tweet.text, 'sentiment_score': analysis.sentiment})
            feeds.append(tweet.text)



    return render_template('feed.html', feed=feeds)

if __name__ == "__main__":
    APP.run(debug=True)