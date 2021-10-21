from src.card import Card
from src.deck import Deck


class Player:
    def __init__(self, addr: tuple[str, int]) -> None:
        self.__cards: list[Card] = []
        self.__score: int = 0
        self.__addr: tuple[str, int] = addr

    def add_card(self, card: Card) -> None:
        self.__cards.append(card)
        card_score = card.get_score()
        if card_score == 11 and self.__score > 10:
            card_score = 1
        self.__score += card_score

    def take_card(self, deck: Deck) -> None:
        card = deck.provide_card()
        self.add_card(card)

    def display_card(self) -> str:
        cards_str = ""
        for card in self.__cards:
            cards_str += str(card) + " "
        return cards_str

    @property
    def address(self) -> tuple[str, int]:
        return self.__addr

    @property
    def score(self) -> int:
        return self.__score

    @property
    def cards(self) -> list[Card]:
        return self.__cards

    def __eq__(self, other) -> bool:
        return self.__addr == other.__addr
