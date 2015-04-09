#!python2

import sys

from bs4 import BeautifulSoup
import requests
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
    print(tuple_list)
    scores = get_scores(tuple_list)
    avg_score = sum(score for _, score in scores.values()) / len(scores)

    for title, score in scores.values():
        print "%s: %f" % (title, score)
    print "Average score: %f" % avg_score

def find_articles(site, terms):
    """Return articles from site matching terms."""
    search = "site:{} {}".format(site, " ".join(terms))
    result = requests.get("https://duckduckgo.com/html/", params={"q": search},
        headers={"User-Agent": "moo"})
    soup = BeautifulSoup(result.text)
    links = [link.get("href") for link in soup.find_all("a")]
    links = [link.get("href") for link in soup.find_all("a")
        if link.get("href") and (link.get("href").startswith("https://" + site)
        or link.get("href").startswith("http://" + site))]
    results = []
    for link in links:
        article = requests.get(link)
        if article.status_code == 200:
            soup = BeautifulSoup(article.text)
            results.append((link, soup.title.string, soup.get_text()))
    return results

if __name__ == "__main__":
    results = find_articles(sys.argv[1], sys.argv[2:])
    newinput(sys.argv[1], results)

if False:
    ##__name__ == '__main__':
    examples = [
        ("http://example.com/1", "Article 1", "This is very good"),
        ("http://example.com/2", "Article 2", "This is very bad"),
        ("http://example.com/3", "Article 3", "This is neutral"),
    ]
    newinput("Example", examples)
