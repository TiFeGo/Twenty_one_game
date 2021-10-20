import pytest
from context import src
from src.card import Card


def test_get_score_digits():
    c = Card(6, "")
    assert c.get_score() == 6


def test_get_score_ace():
    c = Card("Ace", "")
    assert c.get_score() == 11


def test_get_score_king():
    c = Card("King", "")
    assert c.get_score() == 4


def test_get_score_queen():
    c = Card("Queen", "")
    assert c.get_score() == 3


def test_get_score_jack():
    c = Card("Jack", "")
    assert c.get_score() == 2