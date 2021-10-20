import random
from src.card import Card


class Deck:
    def __init__(self) -> None:
        self.__deck: list[Card] = []
        self.__suits: tuple = ("clubs", "diamonds", "hearts", "spades")
        self.__values: tuple = (6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace")

    def init_deck(self) -> None:
        for suit in self.__suits:
            for value in self.__values:
                self.__deck.append(Card(value, suit))

    def provide_card(self) -> Card:
        while True:
            card = random.choice(self.__deck)
            if not card.used:
                card.used = True
                return card

    def get_deck(self) -> list[Card]:
        return self.__deck
