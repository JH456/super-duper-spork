"""
Super Duper Spork
Command line interface for working with the wiki summarize module.

Usage:
    python3 super_duper_spork.py <article name>
"""

from sys import argv
import wiki_summarize

if __name__ == '__main__':
    if len(argv) != 2:
        print(__doc__)
    else:
        search_term = wiki_summarize.prepare_search_term(argv[1])
        markup = wiki_summarize.fetch_article(search_term)
        print(wiki_summarize.is_page_article(markup))
