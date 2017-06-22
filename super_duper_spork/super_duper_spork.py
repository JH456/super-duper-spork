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
    line_length = 2
    line = '| '
    for word in words:
        if line_length + len(word) + 1 <= 79:
            line_length += len(word) + 1
            line += word + " "
        else:
            print(line + ' ' * (79 - line_length) + '|')
            line = '| ' + word + ' '
            line_length = len(word) + 3
    if line != '':
        print(line + ' ' * (79 - line_length) + '|')

def print_article_summary(markup):
    sections = wiki_summarize.extract_sections(markup)
    for title, text in sections:
        print('+' + '-' * 78 + '+')
        print80(title)
        print('+' + '-' * 78 + '+')
        print80(wiki_summarize.summarize_text(text))
    print('+' + '-' * 78 + '+')

def print_disambiguation(markup):
    print('+' + '-' * 78 + '+')
    print80("Your search may refer to:")
    print('+' + '-' * 78 + '+')
    for suggestion in wiki_summarize.get_disambiguation_results(markup):
        print80("- " + suggestion)
    print('+' + '-' * 78 + '+')

def print_search_suggestions(markup):
    print('+' + '-' * 78 + '+')
    print80("No article found! Here are some suggestions:")
    print('+' + '-' * 78 + '+')
    for suggestion in wiki_summarize.get_search_results(markup):
        print80("- " + suggestion)
    print('+' + '-' * 78 + '+')

if __name__ == '__main__':
    if len(argv) != 2:
        print(__doc__)
    else:
        markup = wiki_summarize.fetch_article(argv[1])
        if wiki_summarize.is_page_search_results(markup):
            print_search_suggestions(markup)
        elif wiki_summarize.is_page_disambiguation(markup):
            print_disambiguation(markup)
        else:
            print_article_summary(markup)
