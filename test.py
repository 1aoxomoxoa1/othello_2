from model.board import Board
from controllor.game_controller import GameController
from view.board_console_view import BoardConsoleView
from view.game_console_view import GameConsoleView
from model.players import Players
from model.reversi_game import ReversiGame

#TESTING----
# newBoard = Board(8)

# for row in newBoard.board: 
#     print(row)

# # tup = newBoard.convert_to_tup('D4')
# # print(tup)

# print(newBoard.get_item(3,3))

# console_view = BoardConsoleView(newBoard)
# console_view.draw_board()

# txt2 = "My name is {0}, I'm {1}".format("John",36)
# print(txt2)



new_board2 = Board(4)

game = ReversiGame(4)
board_view = BoardConsoleView(new_board2)
#board_view = 

game_view = GameConsoleView(game, board_view)
#game_view = GameConsoleView(game, Board_view(game.board))

my_controller = GameController(game, game_view) #this should start the game 


my_controller.run()


# game = ReversiGame() 
# view = GameConsoleView(game)
