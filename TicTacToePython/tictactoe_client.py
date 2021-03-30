from tictactoe_state import TicTacToeState
from tictactoe_exceptions import TicTacToeException


class TicTacToeClient():
    def __init__(self, first_player):
        self.state = TicTacToeState()
        self.current_player = first_player

    def move(self, player_id: int, coord: (int, int)):
        try:
            self.state.update_state(player_id, coord)
            if self.current_player == 1: self.current_player = 2
            else: self.current_player = 1
            return coord
        except TicTacToeException as e:
            print(e)

    def get_state(self):
        return self.state.get_inner_state()
    
    def is_ended(self):
        s = self.state.get_inner_state()  

        if 0 not in s.values():
            return True

        if s[(0, 0)] == s[(0, 1)] == s[(0, 2)]  == 1:
            return True
        if s[(1, 0)] == s[(1, 1)] == s[(1, 2)] == 1:
            return True
        if s[(2, 0)] == s[(2, 1)] == s[(2, 2)] == 1:
            return True
        if s[(0, 0)] == s[(1, 0)] == s[(2, 0)] == 1:
            return True
        if s[(0, 1)] == s[(1, 1)] == s[(2, 1)] == 1:
            return True
        if s[(0, 2)] == s[(1, 2)] == s[(2, 2)] == 1:
            return True
        if s[(0, 0)] == s[(1, 1)] == s[(2, 2)] == 1:
            return True
        if s[(0, 2)] == s[(1, 1)] == s[(2, 0)] == 1:
            return True

        if s[(0, 0)] == s[(0, 1)] == s[(0, 2)] == 2:
            return True
        if s[(1, 0)] == s[(1, 1)] == s[(1, 2)] == 2:
            return True
        if s[(2, 0)] == s[(2, 1)] == s[(2, 2)] == 2:
            return True
        if s[(0, 0)] == s[(1, 0)] == s[(2, 0)] == 2:
            return True
        if s[(0, 1)] == s[(1, 1)] == s[(2, 1)] == 2:
            return True
        if s[(0, 2)] == s[(1, 2)] == s[(2, 2)] == 2:
            return True
        if s[(0, 0)] == s[(1, 1)] == s[(2, 2)] == 2:
            return True
        if s[(0, 2)] == s[(1, 1)] == s[(2, 0)] == 2:
            return True

        return False