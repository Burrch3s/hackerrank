#!/bin/python3
"""
https://www.hackerrank.com/challenges/ctci-ransom-note/problem
"""

def check_magazine(magazine, note):
    """Utilizing list builtin, remove all words in note, one at a time, from magazine.
    If a word never existed, existed with incorrect punctuation, or there are not enough
    instances of that word in magazine, then ValueError is raised."""
    tmp = magazine.copy()
    for word in note:
        try:
            tmp.remove(word)
        except ValueError:
            print('No')
            return

    print('Yes')
    return

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    m = int(first_multiple_input[0])
    n = int(first_multiple_input[1])
    mag_list = input().rstrip().split()
    note_list = input().rstrip().split()

    check_magazine(mag_list, note_list)
