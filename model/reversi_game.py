from model.board import Board
from model.players import Players
from model.reversi_user import ReversiUser

class ReversiGame:
    """Represents game. Including board, players, 
        classical rules, alternative rules.
    """

    OTHER_PLAYER = 3


    def __init__(self, size):
        board_size = size
        # rules = ReversiUser.get_rules()
        # self.rules = rules

        self.board = Board(size)
        self.player_x = Players.X
        self.player_y = Players.O
        

        #X goes first
        self.curr_player = ''
   

    def change_player(self):
        """Changes player, used for each turn of the game.
        """
        if self.curr_player == '': 
            self.curr_player = Players.X
        elif self.curr_player == Players.X:
            self.curr_player = Players.O 
        else: 
            self.curr_player = Players.X
           


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
        """Function will return True if either player has a valid move the current player; return False is NO MOVES EXIST
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



    def get_scores(self):
        """Calculates scores for each user. 
        """
        black_score = 0
        white_score = 0
        for r in range(self.board.size):
            for c in range(self.board.size):
                if self.board[r][c] == Players.BLACK_DISK:
                    black_score += 1
                if self.board[r][c] == Players.WHITE_DISK:
                    white_score += 1

        self.score_book = {"X score": black_score, "O score": white_score}
        

    def is_terminated(self):
        """Function will return TRUE if game is terminated, game is terminated if neither player has any legal moves 
        """
        
        if self.board.is_full() == True or self.exist_valid_moves() == False: #if the board is full or no valid moves exist,
            return True #THEN THE GAME IS OVER
        else: #else
            return False #continue the game


        
