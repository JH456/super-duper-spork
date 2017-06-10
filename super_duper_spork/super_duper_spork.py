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
            sections = wiki_summarize.extract_sections(markup)
            for title, text in sections:
                print('+' + '-' * 79)
                print('| ' + title)
                print('+' + '-' * 79)
                print(text)
        else:
            print('+' + '-' * 79)
            print("| No article found! Here are some suggestions:")
            print('+' + '-' * 79)
            for suggestion in wiki_summarize.get_search_results(markup):
                print("| - " + suggestion)
            print('+' + '-' * 79)
