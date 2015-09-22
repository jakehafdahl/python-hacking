#!/usr/bin/env python3
"""Retrieve and print words from a URL.
    
Usage:
    
    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL.
        
    Args:
        url: the URL of a UTF-8 text document
        
    Returns:
        A list of strings containing the words from the document.
    """
    with urlopen(url) as story:
        story_words = [];
        for line in story:
            line_words = line.decode('UTF-8').split()
            for word in line_words:
                story_words.append(word)
        return story_words


def print_words(story_words):
    for word in story_words:
        print(word)


def main(url):
    words = fetch_words(url)
    print_words(words)


if __name__ == '__main__':
    url = sys.argv[1] # The 0th argument is the module filename.
    main(url)
