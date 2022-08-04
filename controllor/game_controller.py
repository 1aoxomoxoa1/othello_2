from re import X
from model.reversi_game import ReversiGame
from model.players import Players
from view.board_console_view import BoardConsoleView
from view.game_console_view import GameConsoleView
from model.invalid_move_error import InvalidMoveError

class GameController: 
    def __init__(self, model: ReversiGame, view: GameConsoleView) -> None:
        self.model = model
        self.view = view

        #think -- game contorller has consoleview: but wait -- something must set up the ConsoleView which contains everything
        #leave as things that i pass in
        # OR: 
        #initialize objects as they are created 

        #in this case: 
        #ReversiGame is factory objcet, creates the objects and then the GameController runs 


# ------General Idea of Run---------
    # def run(self): 
    #     Loop 
    #         which Players
    #         if len(legal_actions == 0): 
    #             if self.game_over(): 
    #                 winner, score diff = self.board.get_winner
    #                 break
    #             else
    #                 continue
        
    #         action = view.get_move() 

    def run(self): 
        
            #need a game console view in the controller that stores the actual BOARD being initialize in the first step of game
            
            board_view = BoardConsoleView(self.model.board)
            game_console_view = GameConsoleView(self.model, board_view)

            self.model.change_player() #first player is set
            game_console_view.draw_board() #board is drawn
            game_console_view.describe_turn() #turn is described, given layer


            while not self.model.is_terminated(): #while game not terminated 
                

                try: 
                    action = game_console_view.get_player_action()
                    if action != 'pass': 
                        row, col = action[0], action[1]
                        print(row, col)

                        if not self.model.is_valid_move(row, col): #if move is valid
                            raise InvalidMoveError
                        else:
                            self.model.make_move(row, col)
                            game_console_view.draw_board()
                    else: #if 'pass', change player
                        pass

                    self.model.change_player()
                    game_console_view.describe_turn()

                except InvalidMoveError:
                    print("Sorry, invalid move")
                    continue


                # print(row, col)
                # print(self.model.board.get_item((4,3)))
                
                 




            #make sure choose move and see them on board
            #then check if they are valid
            
            # legal_actions = list(self.model.board.get_legal_actions())

            # try: 
            #     pass
            # except Error: 
            #     break



    def game_over(self): 
        pass
    

