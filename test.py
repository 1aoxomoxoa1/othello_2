from model.board import Board
from controllor.game_controller import GameController
from view.board_console_view import BoardConsoleView
from view.game_console_view import GameConsoleView
from model.players import HumanPlayer, AiPlayer
from model.reversi_game import ReversiGame


size = int(input('Please enter the size nxn preference for your board: '))
choice = int(input(f'Please select your choice:\n 1) for player vs player \n 2) for player vs simple ai \n 3) for player vs complex ai \n type number here:'))

if choice == 1: 
    game = ReversiGame(size, HumanPlayer.X, HumanPlayer.O, choice)
elif choice == 2: 
    game = ReversiGame(size, HumanPlayer.X, AiPlayer.O, choice)
elif choice == 3: 
    depth = int(input("Please enter the depth (amnount to lookahead) for complex AI: "))
    game = ReversiGame(size, HumanPlayer.X, AiPlayer.O, choice, depth)


game_view = GameConsoleView(game, BoardConsoleView(game.board))
my_controller = GameController(game, game_view) #this should start the game 


my_controller.run()


# game = ReversiGame() 
# view = GameConsoleView(game)
