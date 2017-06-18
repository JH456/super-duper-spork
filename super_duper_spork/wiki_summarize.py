"""
Wiki Summarize
This module is for performing a search on wikipedia for an article, and printing
a summary of it.

Depends on bs4 and nltk.

Functions:
fetch_article which fetches an article
is_page_article which analyzes markup to determine if a page is an article
get_search_results which extracts search results from markup
extract_sections which gets the sections out of article markup
summarize_text which summarizes text

"""

from bs4 import BeautifulSoup
import urllib.request
import nltk
import string

search_url = 'http://wikipedia.org/w/index.php?search='

def fetch_article(search_term):
    """
    Fetches an article from wikipedia using urllib.

    Keyword arguments:
    search_term -- the search term.

    Returns:
    A String containing the page markup.

    """

    def prepare_search_term(search_term):
        return search_term.replace(' ', '+')


    search_term = prepare_search_term(search_term)
    response = urllib.request.urlopen(search_url + search_term)
    return response.read()

def is_page_article(markup):
    """
    Determines if the given markup is for an article or search results page.

    Keyword arguments:
    markup -- a string containing the markup for the page

    Returns:
    True if the page is an article, or false if it is a search results page.

    """

    soup = BeautifulSoup(markup, 'html.parser')

    return soup.title.string.find('Search results') < 0

def get_search_results(markup):
    """
    Gets the search results from a search results page.

    Keyword arguments:
    markup -- a string containing the markup for the page

    Returns:
    An array of strings that are search suggestions. At most 20 in length.

    """

    soup = BeautifulSoup(markup, 'html.parser')

    anchorTags = soup.select('div.mw-search-result-heading a')

    return list(map(lambda x: x.attrs['title'], anchorTags))

def extract_sections(markup):
    """
    Gets a list of tuples in the form (title, text) for each article section.

    Returns:
    [(string, string)]

    """
    soup = BeautifulSoup(markup, 'html.parser')
    contents = soup.select_one('.mw-parser-output').contents
    text = []
    title = soup.select_one('#firstHeading').get_text()
    title_text_map = []
    for content in contents:
        if content.name == 'h2':
            title_text_map.append((title, ''.join(text)))
            text = []
            title = content.get_text()
        elif content.name == 'p':
            text.append(content.get_text())
    return list(filter(lambda e: e[1] != '', title_text_map))

def summarize_text(text):
    """
    Summarizes text

    Keyword arguments:
    text -- string

    Returns:
    A string which is the summarized text.

    """

    words = nltk.word_tokenize(text)
    sentences = nltk.sent_tokenize(text)

    stop_words = set(nltk.corpus.stopwords.words('english'))

    clean_words = [word for word in words
            if word.lower() not in string.punctuation
            and word.lower() not in stop_words]

    print(clean_words)

    return ''

