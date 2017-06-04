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
