class ReversiUser:
    """User Interface called when Reversi Game is run.
    """
    def get_board_size():
        """Retreives board size from user
        """
        board_size = int(input("Enter the board size: "))
        return board_size 

    def get_rules():
        """Retrieves rules for game from user
        """
        rules = input("Enter the game type (classical, alternative): ")
        return rules

    def get_AI():
        pass