# -*- coding: utf-8 -*-
"""
Created on Sat May 20 12:22:30 2017

@author: mustafa
"""
from unittest import TestCase

class IsogramTestCases(TestCase):
  def test_checks_for_isograms(self):
    word = 'abolishment'
    self.assertEqual(
      is_isogram(word),
      (word, True),
       msg="Isogram word, '{}' not detected correctly".format(word)
    )

  def test_returns_false_for_nonisograms(self):
    word = 'alphabet'
    self.assertEqual(
      is_isogram(word),
      (word, False),
      msg="Non isogram word, '{}' falsely detected".format(word)
    )

  def test_it_only_accepts_strings(self):
    with self.assertRaises(TypeError) as context:
      is_isogram(2)
      self.assertEqual(
        'Argument should be a string',
        context.exception.message,
        'String inputs allowed only'
      )

def is_isogram(word):
    '''This function tests for isogram'''
    word_set = set(word)

    if word.strip() == "":
        return (word, False)

    elif len(word) == len(word_set):
        return (word, True)

    elif type(word)!= str :
        raise TypeError

    else:
        return (word, False)