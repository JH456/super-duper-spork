"""
Super Duper Spork
Command line interface for working with the wiki summarize module.

Usage:
    python3 super_duper_spork.py <article name>
"""

from sys import argv
import wiki_summarize

def print80(text):
    words = text.split(' ')
    line_length = 0
    line = ''
    for word in words:
        if line_length + len(word) + 1 <= 80:
            line_length += len(word) + 1
            line += word + " "
        else:
            print(line)
            line = word + ' '
            line_length = len(word) + 1
    if line != '':
        print(line)

def print_article_summary(markup):
    sections = wiki_summarize.extract_sections(markup)
    for title, text in sections:
        print('+' + '-' * 79)
        print('| ' + title)
        print('+' + '-' * 79)
        print80(text)

def print_search_suggestions(markup):
    print('+' + '-' * 79)
    print("| No article found! Here are some suggestions:")
    print('+' + '-' * 79)
    for suggestion in wiki_summarize.get_search_results(markup):
        print("| - " + suggestion)
    print('+' + '-' * 79)

if __name__ == '__main__':
    if len(argv) != 2:
        print(__doc__)
    else:
        markup = wiki_summarize.fetch_article(argv[1])
        if wiki_summarize.is_page_article(markup):
            print_article_summary(markup)
        else:
            print_search_suggestions(markup)
