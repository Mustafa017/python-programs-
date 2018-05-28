# -*- coding: utf-8 -*-
"""
Created on Tue May 23 12:24:58 2017

@author: mustafa
"""

def find_longest_word(text):
    longest_word = max(text.split(), key = len)
    return longest_word, len(longest_word)
print(find_longest_word("This is Andela"))

def longest(sentence):
    words = sentence.split()
    long = max(words, key = len)
    return long
print(longest("This is Andela"))

def find_longest_word(text):
    longest = 0
    for words in text.split():
        if len(words) > longest:
            longest = len(words)
            longest_word = words
    return longest_word, len(longest_word)

def main():
    input_string = input("Please input a list of words to evaluate: ")
    longest_word = find_longest_word(input_string)
    print("The longest word is", longest_word, "with length", len(longest_word))
main()