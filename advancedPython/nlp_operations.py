# Quick Sentiment Score on Tweets
from textblob import TextBlob  
print([TextBlob(tweet).sentiment.polarity for tweet in open("tweets.txt")])

#  Create Word Clouds from Annual Reports
from wordcloud import WordCloud  
WordCloud().generate(open("10K.txt").read()).to_file("cloud.png")

# Keyword Frequency Counter 
import requests; from collections import Counter  
print(Counter(requests.get("https://competitor.com").text.lower().split()))