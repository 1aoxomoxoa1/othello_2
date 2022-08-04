from model.players import Players


class Board:
    EMPTY_CELL = '' 

    def __init__(self, size):
        """Initializes board attributes

        Args:
            size(int) = user input size 
        """
        self.size = size

        #allocate the board with empty squares 
        self.board = [[self.EMPTY_CELL] * size for _ in range(size)]
        
        #initialize starting positions
        self.mid = size // 2
        self.board[self.mid-1][self.mid] = 'X'
        self.board[self.mid - 1][self.mid - 1] = 'O'
        self.board[self.mid][self.mid - 1] = 'X'
        self.board[self.mid][self.mid] = 'O'

    
    def update_cell(self, row, column, player):
        self.board[row][column] = player


    def get_item(self, index):
        """Added board[][] undex syntax
        index: subscript index as TUPLE
        return: value 'X', 'O', or '' at index
        """
        x,y = index[0], index[1]
        return self.board[x][y]


    def convert_to_tup(self, action): 
        """Convert the input that comes in as a string into a tuple representing indices of matrix
        Args: 
            action {str} -- ex1) 'A1'  ex2) 'B4'
        Ret: 
            action {tup} ex1) (0,0) ex2) (3,1)
        """
        row, col = str(action[1]).upper(), str(action[0]).upper()

        if row in '12345678' and col in 'ABCDEFGH': #if row and col exist in selection area

            x, y = '12345678'.index(row), 'ABCDEFGH'.index(col)
            return x, y 


    def update_location(self, row, col, player):
        """Updates board location
        
        Args:
            row(list): row index of board matrix
            col(list): column index of board matrix
            player(Players): the current player -- either 'X' or 'O'
        """
        if player == Players.WHITE_PLAYER:
            self.board[row][col] = 'X'
        else: 
            self.board[row][col] = 'O'


    def is_valid_location(self, row, col):
        """Returns True/False if row, col are within board range 

        Args:
            row(list): row index of board matrix
            col(list): column index of board matrix
        """
        return row >= 0 and row <= self.size - 1 and col >= 0 and col <= self.size - 1


    #-------TO DELETE----------
    # def is_valid_move(self, action, color): 
    #     """Will return TRUE if player can move to place (xstart, ystart)
    #     If it is valid move, returns list of spaces that would become players if they move there
    #     Args:
    #         action: {str} desired move location
    #         color: {intenum} color of player who is moving
    #     """

    #     if isinstance(action, str): #action
    #         action = self.convert_to_tup(action) #convert string to tup
        
    #     xstart, ystart = action #get indices from tupp.

    #     if self.board[xstart][ystart] != '' or not self.is_valid_location(xstart, ystart): #if choice isnt valid on board or open
    #         return False

    #     #put color in selected move temporarily
    #     self.board[xstart][ystart] = color

    #     #set opponent color
    #     op_color = 'O' if color == 'X' else 'X'

    def count_tiles(self): 
        """ same func as num_disks()
        """
        tiles = {}  # key = player symbol, value = disks number

        #iterate through matrix
        for row in self.board:
            for i in row:
                if i in tiles: #if already in return dict
                    tiles[i] += 1 #add to certain 
                else:
                    tiles[i] = 1
        return tiles

    def is_full(self):
        """Go through each cell and see if empty. 
        Args:
            n/a
        Return:
            TRUE if cells are EMPTY
            FALSE if cells are NOT EMPTY
        """
        for row in self.board:
            if self.EMPTY_CELL not in row:
                pass
            else:
                return False
        return True









    # def get_legal_actions(self, player): 
    #     """
    #     Legal moves to obtain pieces according to the rules of Othello
    #     :param color: different colored pieces, X-black, O-white
    #     :return: Generate legal move coordinates, use list() method to get all legal coordinates
    #     """
    #     # Indicates the 8 different direction coordinates of the chessboard coordinate point, for example, the direction coordinate [0][1] means directly above the coordinate point.
    #     direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    #     op_color = "O" if player == 'X' else 'X'
    #     # Count the positions of the unsettled states adjacent to the op_color side
    #     op_color_near_points = []

    #     board = self._board
    #     for i in range(8):
    #         for j in range(8):
    #             if board[i][j] == op_color:
    #                 for dx, dy in direction:
    #                     x, y = i + dx, j + dy
    #                     if 0 <= x <= 7 and 0 <= y <= 7 and board[x][y] == self.empty and (
    #                             x, y) not in op_color_near_points:
    #                         op_color_near_points.append((x, y))
    #     l = [0, 1, 2, 3, 4, 5, 6, 7]
    #     for p in op_color_near_points:
    #         if self._can_fliped(p, player):
    #             if p[0] in l and p[1] in l:
    #                 p = self.num_board(p)
    #             yield p        


