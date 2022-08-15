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


    def test_simple_ai_pick_best_move(self): 
        """if call this test test_ai_picks_valid_move() 
        """
        my_game = ReversiGame(4, HumanPlayer.X, AiPlayer.O, 2)
        my_game.curr_player = AiPlayer.O
        expected_moves = my_game.get_best_moves() 
        #[(0,2), (2,0), (1,3), (3,2)]

        self.assertTrue(my_game.get_simple_ai_move() in expected_moves) #should be on of lst of moves



class TestBoard(unittest.TestCase): 

    @classmethod
    def setUpClass(cls):
        cls.board = Board()
        #can reference this in other test_functions by saying (self.board)
    
    def test_board(self): 
        board = Board(4)
        self.assertEqual(board.get_item((1,1)), 'O') 

