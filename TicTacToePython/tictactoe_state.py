from tictactoe_exceptions import IllegalMoveException
from tictactoe_exceptions import IllegalPlayerIDException
from tictactoe_exceptions import IllegalCoordinateException


class TicTacToeState(object):
    def __init__(self, state:dict=None):
        self._inner_state = self.initialize_state(state)
        self.hash = self.get_inner_state

    def initialize_state(self, state:dict=None) -> dict:
        if state != None:
            out = dict()
            for k, v in state.items():
                out[k] = v
            return out
        state = {}
        for x in range(3):
            for y in range(3):
                state[(x, y)] = 0
        return state
    
    def update_state(self, player_id: int, coord: (int, int)) -> None:
        ''' Checks if the inner field at coord is free and sets it according to
            player_id or throws an exception.

            Parameters:
            player_id: The id of the player that made the move. (1 or 2)
            coord: Coordinate of the field the move was made on. Both X and Y
                are integers between 0 and 2.
        '''

        if coord not in self._inner_state.keys():
            raise IllegalCoordinateException(coord)
        if self._inner_state[coord] != 0:
            raise IllegalMoveException(player_id, coord)
        if player_id not in (1, 2):
            raise IllegalPlayerIDException(player_id)
        
        self._inner_state[coord] = player_id
    
    def get_inner_state(self):
        ''' Returns a read-only version of the inner state.
        '''
        return self._inner_state

    def __str__(self) -> str:
        tmp = []
        for k, v in self._inner_state.items():
            tmp.append('{}: {}'.format(k, v))
        return '\n'.join(tmp)
