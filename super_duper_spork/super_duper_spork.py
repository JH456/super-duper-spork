"""
Super Duper Spork
Command line interface for working with the wiki summarize module.

Usage:
    python3 super_duper_spork.py <article name>
"""

from sys import argv
from wiki_summarize import prepare_search_term

if __name__ == '__main__':
    if len(argv) != 2:
        print(__doc__)
    else:
        search_term = argv[1]
        print(prepare_search_term(search_term))
