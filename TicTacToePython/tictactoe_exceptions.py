class TicTacToeException(Exception):
    def __init__(self, message):
        super().__init__(message)


class IllegalMoveException(TicTacToeException):
    def __init__(self, player_id, coord, message="A player is trying to make a move on an already occupied field."):
        self.player_id = player_id
        self.coord = coord
        super().__init__(message)


class IllegalPlayerIDException(TicTacToeException):
    def __init__(self, player_id, message="player_id has to be 1 or 2."):
        self.player_id = player_id
        super().__init__(message)


class IllegalCoordinateException(TicTacToeException):
    def __init__(self, coord, message="X and Y coordinates can only be one of the following numbers: (0, 1, 2)"):
        self.coord = coord
        super().__init__(message)