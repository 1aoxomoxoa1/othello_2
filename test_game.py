import unittest
from model.reversi_game import ReversiGame
from model.players import AiPlayer, HumanPlayer, Players
from model.board import Board

class TestAi(unittest.TestCase): 


    def test_simple_ai(self): 
        """if call this test test_ai_picks_valid_move() 
        """
        my_game = ReversiGame(4, HumanPlayer.X, AiPlayer.O, 2)
        my_game.curr_player = AiPlayer.O
        expected_moves = my_game.get_valid_moves()         
        self.assertTrue(my_game.get_simple_ai_move() in expected_moves) #simple ai should be in lst of valid_moves


    def test_complex_ai(self): 
        """will test to see if the complex_ai picks from one of the valid moves
        """
        my_game = ReversiGame(4, HumanPlayer.X, AiPlayer.O, 5) #set depth to 5
        my_game.max_depth = 5 #need to set a variable in object same to depth we have
        my_game.curr_player = AiPlayer.O
        expected_moves = my_game.get_valid_moves()
        self.assertTrue(my_game.minimax() in expected_moves) #test succeeds if move returned from minimax is in expected_moves



class TestBoard(unittest.TestCase): 

    @classmethod
    def setUpClass(cls):
        cls.board = Board()
        #can reference this in other test_functions by saying (self.board)
    
    def test_board(self): 
        board = Board(4)
        self.assertEqual(board.get_item((1,1)), 'O') 

