from model.reversi_game import ReversiGame
from view.game_view import GameView
from view.board_console_view import BoardConsoleView
from view.game_view import GameView

class GameConsoleView(GameView):
    
    #symbols used to describe different players
    symbols = {0: ' ', 1: 'X', 2: 'O'}


    def __init__(self, game: ReversiGame, board_view: BoardConsoleView) -> None:
        self.game = game
        self.board_view = board_view


    def describe_turn(self):
        print(f'Player {self.symbols[self.game.curr_player]}: It\'s your turn')
        print('To cancel the move enter \"pass\"')


    def get_player_action(self): 
        """Function returns gets the input from player on turn and then returns the move as tup 
        Args: 
            game
        Ret: 
            move {tup} of (row, col) 
        """
        str = input('Enter your move (row, col):')
        move = str.split(',') 
        if move[0] != "pass":
            row, col = int(move[0]) - 1, int(move[1]) - 1
            return (row, col)
        else:
            return "pass"


    def draw_board(self):
        """_summary_ WILL DRAW BOARD FOR EACH TURN, RETURNS FALSE if the game is over

        Returns:
            BOOL: game_over_bool if the game is over when the board is being drawn
        """
        self.board_view.draw_board()

        #makes a dict storing x's count in [1] , o's count in [2]
        num_disks = self.game.board.count_tiles()
        if not self.game.is_terminated():
            items = num_disks.items()
            x_score = num_disks['X']
            x_str = f'X score: {x_score}, '
            o_score = num_disks['O']
            o_str = f'O score: {o_score}'
            print(x_str + o_str)
        else: 
            return True

            # for key, value in items: 
            #     if key == 'X': 
            #         x_score = num_disks['X']
            #         x_str = f'X score: {x_score}, '
            #     if key == 'O':
            #         o_score = num_disks['O']
            #         o_str = f'O score: {o_score}'

            #     print(x_score + o_score)
            #----------------------------------------
            #print(f'X score: {list(num_disks.values())[1]}, O score: {list(num_disks.values())[2]} ')



    def display_winner(self):
        num_disks = self.game.board.count_tiles()
        x_score = num_disks['X']
        x_str = f'X score: {x_score}, '
        o_score = num_disks['O']
        o_str = f'O score: {o_score}'
        
        if x_score > o_score: 
            win_str = f'Congrats, X -- Player X: {x_score} Player O: {o_score}'
        elif x_score < o_score:
            win_str = f'Congrats, O -- Player X: {x_score} Player O: {o_score}'
        else: 
             win_str = f'Its a tie! -- Player X: {x_score} Player O: {o_score}'
        print(win_str)


        pass
    
    def wrong_cell(self):
        print("Invalid location, try again")

    def value_error_msg(self):
        print("Invalid move, try again")



