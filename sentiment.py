from textblob import TextBlob


def get_polarity(text):
    return TextBlob(text).sentiment.polarity

print get_polarity("hello!")
