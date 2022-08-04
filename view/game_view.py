from abc import ABC, abstractmethod
from model.reversi_game import ReversiGame


class GameView(ABC):
    def __init__(self, game: ReversiGame) -> None:
        self.game = game

    @abstractmethod
    def get_player_action(self):
        pass

    @abstractmethod
    def draw_board(self):
        pass

    @abstractmethod
    def display_winner(self, player):
        pass