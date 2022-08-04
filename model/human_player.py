from players import Players
from board import Board

class HumanPlayer(Players): 
    """This represents a human player -- non-AI
    """
    def __init__(self) -> None:
        """Initiates the color as either 'X' or 'O'
        """


    # def get_move(self, board: Board):
    #     #establish whether player is X or O 
    #     if board.color == "X":
    #         player = '[H] BLACK'
    #     else:
    #         player = '[H] WHITE'

    #     print('Player ' + self.color + ': it\'s your turn')
    #     while True: 
    #         action = input("Please enter your move: (row, col) ")
    #         move_lst = action.split(',')
    #         action_tup = int(move_lst[0]), int(move_lst[1]) #tupple storing the move int ints (row, col)
    #         if action_tup[0] in 123456789 and action_tup[1] in 123456789:

    #             #if action_tup in board.get_legal_actions(self.color): 
    #             return action_tup


            
            