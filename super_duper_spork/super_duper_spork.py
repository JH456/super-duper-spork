"""
Super Duper Spork
Command line interface for working with the wiki summarize module.

Usage:
    python3 super_duper_spork.py <article name>
"""

from sys import argv
import wiki_summarize

def prettify_text(text, max_line_length):
    """
    Adds line endings to a string so each line is of 80 characters each at most.

    Will also add in pipes to pretty print the output.

    Keyword arguments:
    text -- a string of words separated by spaces to pretty print.
    max_line_length -- int

    """
    words = text.split(' ')
    line_length = 2
    line = '| '
    pretty_text = ''
    for word in words:
        if line_length + len(word) + 2 <= max_line_length:
            line_length += len(word) + 1
            line += word + " "
        else:
            pretty_text += line + ' ' * (max_line_length - 1 - line_length) + '|' + '\n'
            line = '| ' + word + ' '
            line_length = len(word) + 3
    if line != '':
        pretty_text += (line + ' ' * (max_line_length - 1 - line_length) + '|')
    return pretty_text

def print_article_summary(markup):
    sections = wiki_summarize.extract_sections(markup)
    for title, text in sections:
        print('+' + '-' * 78 + '+')
        print(prettify_text(title, 80))
        print('+' + '-' * 78 + '+')
        print(prettify_text(wiki_summarize.summarize_text(text), 80))
    print('+' + '-' * 78 + '+')

def print_disambiguation(markup):
    print('+' + '-' * 78 + '+')
    print(prettify_text("Your search may refer to:", 80))
    print('+' + '-' * 78 + '+')
    for suggestion in wiki_summarize.get_disambiguation_results(markup):
        print(prettify_text("- " + suggestion, 80))
    print('+' + '-' * 78 + '+')

def print_search_suggestions(markup):
    print('+' + '-' * 78 + '+')
    print(prettify_text("No article found! Here are some suggestions:", 80))
    print('+' + '-' * 78 + '+')
    for suggestion in wiki_summarize.get_search_results(markup):
        print(prettify_text("- " + suggestion, 80))
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
