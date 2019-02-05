"""
Create a word-list from a given website using BeautifulSoup.
Gets all body text from a webpage and adds all unique words to a set.
Ignoress all style, script, head, and title tags.
"""

from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request


def tags(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def get_body(body):

    word_list = set()

    soup = BeautifulSoup(body, 'html.parser')
    get_body = soup.findAll(text=True)
    visible_texts = filter(tags, get_body) 

    text = u" ".join(t.strip() for t in visible_texts)

    get_words = set(text.split())
    words.update(get_words)

    print(word_list)

html = urllib.request.urlopen('http://www.espn.com/nfl/story/_/id/25921740/super-bowl-liii-was-greatest-defensive-performance-history-here-how-patriots-did-rams').read()

print(get_body(html))
