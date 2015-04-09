#!python2
from textblob import TextBlob


def get_polarity(text):
    return TextBlob(text).sentiment.polarity

def get_scores(articles):
    scores = {}
    for url, title, text in articles:
        scores[url] = title, get_polarity(text)
    return scores

# (url, title, text)
def newinput(source, tuple_list):
    scores = get_scores(tuple_list)
    avg_score = sum(score for _, score in scores.values()) / len(scores)

    for title, score in scores.values():
        print "%s: %f" % (title, score)
    print "Average score: %f" % avg_score

    if avg_score > 0:
        print "%s likes %s" % (source, search_term)
    else:
        print "%s dislikes %s" % (source, search_term)


if __name__ == '__main__':
    search_term = "David Cameron"
    examples = [
        ("http://example.com/1", "Article 1", "This is very good"),
        ("http://example.com/2", "Article 2", "This is very bad"),
        ("http://example.com/3", "Article 3", "This is neutral"),
    ]
    newinput("Example", examples)
