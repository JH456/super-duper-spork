"""
Super Duper Spork
Command line interface for working with the wiki summarize module.

Usage:
    python3 super_duper_spork.py <article name>
"""

from sys import argv

if __name__ == '__main__':
    if len(argv) != 2:
        print(__doc__)
    else:
        article_name = argv[1]
        print('Success!')
