import pytest
from context import src
from src.deck import Deck
from src.card import Card

deck = Deck()
deck.init_deck()

full_deck = [Card(6, "clubs"), Card(7, "clubs"), Card(8, "clubs"), Card(9, "clubs"), Card(10, "clubs"),
             Card("Jack", "clubs"),
             Card("Queen", "clubs"), Card("King", "clubs"), Card("Ace", "clubs"),
             Card(6, "diamonds"), Card(7, "diamonds"), Card(8, "diamonds"), Card(9, "diamonds"), Card(10, "diamonds"),
             Card("Jack", "diamonds"),
             Card("Queen", "diamonds"), Card("King", "diamonds"), Card("Ace", "diamonds"),
             Card(6, "hearts"), Card(7, "hearts"), Card(8, "hearts"), Card(9, "hearts"), Card(10, "hearts"),
             Card("Jack", "hearts"),
             Card("Queen", "hearts"), Card("King", "hearts"), Card("Ace", "hearts"),
             Card(6, "spades"), Card(7, "spades"), Card(8, "spades"), Card(9, "spades"), Card(10, "spades"),
             Card("Jack", "spades"),
             Card("Queen", "spades"), Card("King", "spades"), Card("Ace", "spades")]


def test_deck_size():
    assert len(deck.get_deck()) == 36


def test_deck():
    assert deck.get_deck() == full_deck


def test_provide():
    provided_deck = []
    for _ in range(36):
        provided_deck.append(deck.provide_card())
    assert all(card in provided_deck for card in full_deck)
