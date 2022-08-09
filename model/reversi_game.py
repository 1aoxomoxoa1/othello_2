from model.board import Board
from model.players import Players
from model.reversi_user import ReversiUser
import datetime
import copy
import random

class ReversiGame:
    """Represents game. Including board, players, 
        classical rules, alternative rules.
    """

    OTHER_PLAYER = 3


    def __init__(self, size, player_1, player_2):
        board_size = size

        self.board = Board(size)
        self.player_x = player_1
        self.player_o = player_2
        

        #X goes first
        self.curr_player = ''
   

    def change_player(self):
        """Changes player, used for each turn of the game.
        """
        if self.curr_player == '': 
            self.curr_player = self.player_x
        elif self.curr_player == self.player_x: #if curr_player is already x
            self.curr_player = self.player_o  #change to o
        else: #if already o
            self.curr_player = self.player_x #change to x
           


    def is_valid_move(self, row, col):
        """Determines if inputted move is valid.
        Args: 
            row: row inputted
            col: column inputted
        Returns:
            FALSE -- if the players move is not valid
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        desired_cell = (row, col) #cell we want

        if self.curr_player == Players.X: #set marker depending on who current player is
            player_marker = 'X'
            enemy_marker = 'O'
        else: 
            player_marker = 'O'
            enemy_marker = 'X'

        #check and see there is no value already existing in the cell
        existing_cell_value = self.board.get_item((row,col))
        if existing_cell_value is 'X' or existing_cell_value is 'O': 
            return False

        for direction in directions: 
            curr_cell = desired_cell
            to_update = []
            while self.board.is_valid_location(curr_cell[0] + direction[0], curr_cell[1] + direction[1]): #see if directions is a valid location
                curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1]) #store te location to test

                if self.board.get_item(curr_cell) == enemy_marker: #if surrounded by opponents tile
                    to_update.append(curr_cell) #meaning this is location for current cell is valid 
                elif self.board.get_item((curr_cell[0], curr_cell[1])) == player_marker and len(to_update) > 0:
                    return True
                else: 
                    break
        return False 

    def exist_valid_moves(self): 
        """Function will return true if CURRENT PLAYER has a current move, used to see if player must be assigned pass
        """
        curr_player = self.curr_player

        for i in range(len(self.board.board[0])): 
                for j in range(len(self.board.board)): 
                    if self.board.board[i][j] == '': #if space is empty, check  and see if valid move for either player
                        if self.is_valid_move(i, j): #if move is valid
                            if self.curr_player != curr_player: 
                                self.change_player()
                            return True #we know that A valid move exists
                        else:
                            continue

        return False

    def get_valid_moves(self): 
        """Will return a lst of the valid moves for the player at self.curr_player
        Args:
            n/a
        Ret: 
            moves_lst {list} [(row, col), ] of all of the valid moves for a certain player given the current board
        """

        moves_lst = []
        
        for i in range(len(self.board.board[0])): 
                for j in range(len(self.board.board)): 
                    if self.board.board[i][j] == '': #if space is empty, check  and see if valid move for either player
                        if self.is_valid_move(i, j): #if move is valid
                            moves_lst.append((i,j)) #we know that A valid move exists
                        else:
                            continue
        
        return moves_lst


    def get_simple_ai_move(self):
        """this function will get the best moves for a given game state that the ai will player
        Args:
            n/a
        Ret:
            best_move {_tup_} (row, col) a tupple representing the best move for ai 
        """
        valid_moves = self.get_valid_moves()

        #lst of [((row,col), score=int), .....] for all valid moves
        move_and_score = [] 

        for move in valid_moves:
            score = self.get_score(move)
            move_and_score.append((move, score))
        
        #lst of just the scores
        score_lst = [i[1] for i in move_and_score]

        #get the max of all the scores
        max_score = max(score_lst)
        
        #lst of just the moves with best score
        best_moves = [i[0] for i in move_and_score if i[1] == max_score]

        #if multiple "best moves", get an index at random
        idx = random.randint(0, len(best_moves) - 1)

        return best_moves[idx]



    def get_score(self, move):
            """get_score will return the score for a given move

            Args:
                move (_tup_): (row, col) representing the move that we are checking the score for
            Ret: 
                score (_int_): representing the score of the move we checked (Ai score after - opponent score after)
            """
            if self.curr_player == self.player_x:
                ai_marker = 'X'
                player_marker = 'O'
            elif self.curr_player == self.player_o: 
                ai_marker = 'O'
                player_marker = 'X'

            #make a copy of the board
            copy_of_game = copy.deepcopy(self)

            #make the move in the copied game
            copy_of_game.make_move(move[0], move[1])

            #count it up after move is made
            num_disks = copy_of_game.board.count_tiles()
            
            ai_score = num_disks[ai_marker]
            player_score = num_disks[player_marker]

            return ai_score - player_score




    def exist_any_valid_moves(self): 
        """Function will return True if EITHER player has a valid move the current player; return False is NO MOVES EXIST
        Args:
            player {Player} 'X' or 'O/
        """
        #keep current player when function starts
        curr_player = self.curr_player

        #iter across empty spaces, twice, check if either player has valid move
        for player_num in range(2): 
            if player_num == 1: 
                self.change_player() #change the current player to check for the other player

            for i in range(len(self.board.board[0])): 
                for j in range(len(self.board.board)): 
                    if self.board.board[i][j] == '': #if space is empty, check  and see if valid move for either player
                        if self.is_valid_move(i, j): #if move is valid
                            if self.curr_player != curr_player: 
                                self.change_player()
                            return True #we know that A valid move exists
                        else:
                            continue
        
        #check make sure player is same as start
        if self.curr_player != curr_player: 
            self.change_player()
        return False

    

                


    def make_move(self, row, col):
        """will make the move
        Args: 
            action: {tup} that stores row, col
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)] #direction lst to iterate over
        target_cell = (row, col) #Tup of cell we want to move to 

        #set markers depending on who is making the move
        if self.curr_player == Players.X: 
            enemy_marker = 'O'
            player_marker = 'X'
        else: 
            enemy_marker = 'X'
            player_marker = 'O'

        for direction in directions:
            curr_cell = target_cell

            #to update will store a list of the cells that need to be updated
            to_update = []
            while self.board.is_valid_location(curr_cell[0] + direction[0], curr_cell[1] + direction[1]):
                curr_cell = (curr_cell[0] + direction[0],
                             curr_cell[1] + direction[1])
                if self.board.get_item((curr_cell[0], curr_cell[1])) == enemy_marker:
                    to_update.append(curr_cell)
                elif self.board.get_item((curr_cell[0], curr_cell[1])) == player_marker and len(to_update) > 0:
                    for i in to_update: #for each cell that needs to be updated
                        self.board.update_cell(i[0], i[1], player_marker) #update it with marker from current player!
                else:
                    break
        self.board.update_cell(row, col, player_marker)
        

    def is_terminated(self):
        """Function will return TRUE if game is terminated, game is terminated if neither player has any legal moves 
        """
        
        if self.board.is_full() == True or self.exist_any_valid_moves() == False: #if the board is full or no valid moves exist,
            return True #THEN THE GAME IS OVER
        else: #else
            return False #continue the game


    def write_to_file(self):
        num_disks = self.board.count_tiles()
        x_score = num_disks['X']
        x_str = f'X score: {x_score}, '
        o_score = num_disks['O']
        o_str = f'O score: {o_score}'
        
        if x_score > o_score: 
            win_str = f'Congrats, Player X Wins -- Player X: {x_score} Player O: {o_score}'
        elif x_score < o_score:
            win_str = f'Congrats, Player O Wins -- Player X: {x_score} Player O: {o_score}'
        else: 
             win_str = f'Its a tie! -- Player X: {x_score} Player O: {o_score}'

        now = datetime.datetime.now()
        current_time = now.strftime("%m-%d-%Y %H:%M:%S")
        
        to_write = f'{current_time} -- {win_str}'

        try: 
            with open('winner.txt', 'w') as f:
                f.write(to_write)
        except FileNotFoundError:
            print('Sorry file not found')        
