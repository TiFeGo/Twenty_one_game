from typing import Union


class Card:
    def __init__(self, value: Union[int, str], suit: str) -> None:
        self.__value: Union[int, str] = value
        self.__suit: str = suit
        self.__used: bool = False

    def get_score(self) -> int:
        if self.__value == "Ace":
            result = 11
        elif self.__value == "King":
            result = 4
        elif self.__value == "Queen":
            result = 3
        elif self.__value == "Jack":
            result = 2
        else:
            result = self.__value

        self.__used = False

        return result

    @property
    def used(self) -> bool:
        return self.__used

    @used.setter
    def used(self, flag: bool) -> None:
        self.__used = flag

    def __str__(self) -> str:
        return f"value: {self.__value}, suit: {self.__suit} "

    def __eq__(self, other):
        return self.__value == other.__value and self.__suit == other.__suit 
