from src.player import Player


class GameLogic:

    def win(self, players, dialer) -> list[tuple[Player, str]]:
        result: list[tuple[Player, str]] = []

        for player in players:
            cond = "lose"
            if player.score < 21:
                if player.score > dialer.score:
                    cond = "win"
                elif player.score == dialer.score:
                    cond = "draw"
            elif player.score == 21:
                if player.score == dialer.score:
                    cond = "draw"
                else:
                    cond = "win"
            result.append((player, cond))
        return result
