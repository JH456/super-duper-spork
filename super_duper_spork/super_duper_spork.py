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
        markup = wiki_summarize.fetch_article(argv[1])
        if wiki_summarize.is_page_article(markup):
            sections = wiki_summarize.extract_section_map(markup)
            for key, value in sections:
                print(key)
        else:
            print("+---------------------------------------------")
            print("| No article found! Here are some suggestions:")
            print("+---------------------------------------------")
            for suggestion in wiki_summarize.get_search_results(markup):
                print("| - " + suggestion)
            print("+---------------------------------------------")
