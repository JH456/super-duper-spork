"""
Wiki Summarize
This module is for performing a search on wikipedia for an article, and printing
a summary of it.

Depends on bs4 and nltk.

Functions:
prepare_search_term(search_term) prepares a search term to be put in a url.

"""

from bs4 import BeautifulSoup
import urllib.request

search_url = 'http://wikipedia.org/w/index.php?search='

def prepare_search_term(search_term):
    """
    Prepares search term to be embedded in a url.

    Keyword arguments:
    search_term -- the unprocessed search term to be prepared.

    Returns:
    The prepared search term. For example, "I like pie" -> "I+like+pie"
    
    """
    return search_term.replace(' ', '+')

def fetch_article(search_term):
    """
    Fetches an article from wikipedia using urllib.
    
    Keyword arguments:
    search_term -- the processed search term.

    Returns:
    A String containing the page markup.

    """

    response = urllib.request.urlopen(search_url + search_term)
    return response.read()
