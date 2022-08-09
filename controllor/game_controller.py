from re import X
from model.reversi_game import ReversiGame
from model.players import AiPlayer, HumanPlayer
from view.board_console_view import BoardConsoleView
from view.game_console_view import GameConsoleView
from model.invalid_move_error import InvalidMoveError

class GameController: 
    def __init__(self, model: ReversiGame, view: GameConsoleView) -> None:
        self.model = model
        self.view = view


    def run(self): 
        
            #need a game console view in the controller that stores the actual BOARD being initialize in the first step of game
            
            board_view = BoardConsoleView(self.model.board)
            game_console_view = GameConsoleView(self.model, board_view)

            self.model.change_player() #first player is set
            self.view.draw_board() #board is drawn
            self.view.describe_turn() #turn is described, given layer


            while not self.model.is_terminated(): #while game not terminated 
                

                try: 
                    
                    if self.model.exist_valid_moves(): #if player has valid moves

                        if isinstance(self.model.curr_player, HumanPlayer): 
                            action = self.view.get_player_action()
                        elif isinstance(self.model.curr_player, AiPlayer): 
                            action = self.model.get_simple_ai_move() 

                    else: #if player has no valid moves
                        print("No valid move, passed")
                        action = 'pass' #assign action to 'pass' 
                        
                    if action != 'pass': #if action is not to pass
                        
                        row, col = action[0], action[1]

                        if self.model.is_valid_move(row, col): #if move is a valid move 
                        
                            row, col = action[0], action[1]
                            print(row, col)

                            self.model.make_move(row, col)
                            game_over_bool = self.view.draw_board()  #game_over_bool will turn true if the game is over

                        else: #if it is an invalid move
                            raise InvalidMoveError

                    else: #if 'pass', just draw board
                            pass

                    if game_over_bool: #if game is over
                        break #break from looop
                    else: 
                        self.model.change_player()
                        self.view.describe_turn()

                except InvalidMoveError:
                    print("Sorry, invalid move")
                    continue

        
            self.game_over()
                
                 




            #make sure choose move and see them on board
            #then check if they are valid
            
            # legal_actions = list(self.model.board.get_legal_actions())

            # try: 
            #     pass
            # except Error: 
            #     break



    def game_over(self): 
        self.view.display_winner()
        self.model.write_to_file()

        # file --{Date and time of the game} {which player won (X/O) or a draw} {the score of each player}
    

