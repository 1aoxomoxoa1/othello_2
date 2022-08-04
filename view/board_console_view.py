from model.board import Board
from view.board_view import BoardView

class BoardConsoleView(BoardView):
    """Represents board view in console
    """
    
    #symbols = {0: " ", 1: "X", 2: "O"}
    
    def __init__(self, board: Board) -> None:
        super().__init__(board)

    def draw_board(self):
        board_size = self.board.size + 1
        header = '+---'* (self.board.size + 1)  #header for each row
        surrounding_row = '|   '* (self.board.size + 1) #this will surround each row
        
        top_header = '    '
        for i in range(1, self.board.size + 1):
            if i != self.board.size: 
                top_header += str(i) + '   '
            else: 
                top_header += str(i)
        print(top_header)
        #print('    1   2   3   4   5   6   7   8')
        for row in range(1, self.board.size + 1):
            print(header)
            print(surrounding_row) #above the row that is playable
            # print(str(row) + ' ') #prints row number
            
            return_string = str(row) + ' ' #start of the string that will append values if there are any
            for col in range(0, self.board.size):
                index = (row - 1, col) #tupple for mat index (row, col)
                value = self.board.get_item(index)
                if value == '': #if value not filled
                    return_string += '|   '
                    # print('|   ')  #print blank spot
                else: 
                    return_string += '| ' + str(value) + " "

            return_string += '|'
            print(return_string)
            print(surrounding_row)



