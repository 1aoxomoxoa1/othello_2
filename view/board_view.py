from abc import ABC, abstractmethod
from model.board import Board

class BoardView(ABC):
    """Abstract class that allows you to extrapolate for other views: ex) board_console_view, board_gui_view, etc
    """
    
    #symbols = {0: " ", 1: "X", 2: "O"}
    
    def __init__(self, board: Board):
        self.board = board

    def draw_board(self):
        pass

    