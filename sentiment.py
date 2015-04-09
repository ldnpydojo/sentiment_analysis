from textblob import TextBlob


def get_polarity(text):
    return TextBlob(text).sentiment.polarity


# (url, title, text)
def newinput(source, tuple_list):
    result = []
    score = 0
    for url, title, text in tuple_list:
        polarity = get_polarity(text)
        score += polarity
        result.append((url, title, polarity))
    avg = score / len(tuple_list)
    return result, avg
