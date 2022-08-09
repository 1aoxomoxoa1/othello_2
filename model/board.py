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



    def count_tiles(self): 
        """ Will count the tiles for each player and return a dict {'X': count , 'O': count}
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



