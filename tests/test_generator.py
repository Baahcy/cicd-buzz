import unittest

from buzz import generator


def test_sample_single_word():
    lad = ('foo', 'bar', 'foobar')
    word = generator.sample(lad)
    assert word in lad


def test_sample_multiple_words():
    lad = ('foo', 'bar', 'foobar')
    words = generator.sample(lad, 2)
    assert len(words) == 2
    assert words[0] in lad
    assert words[1] in lad
    assert words[0] is not words[1]


def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5
