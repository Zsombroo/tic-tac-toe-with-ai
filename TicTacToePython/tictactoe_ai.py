import random
import pickle


from tictactoe_client import TicTacToeClient


class TicTacToeAI(object):
    def __init__(self, ai_id: int, game_object: TicTacToeClient):
        self.my_id = ai_id
        self.game_object = game_object
        self.lookup_table = self._load_decision_tree()
    
    def _load_decision_tree(self) -> dict:
        with open('decision_tree.pickle', 'rb') as handle:
            b = pickle.load(handle)
        return b

    def move(self):
        game_state = self.game_object.get_state()
        next_moves = self.lookup_table[str(game_state)]

        if type(next_moves[1]) == int:
            return self.game_object.move(self.my_id, next_moves[0])
        else:
            current_best_value = -2
            current_best_move = None
            for move_tuple in next_moves:
                if move_tuple[1] > current_best_value:
                    current_best_value = move_tuple[1]
                    current_best_move = move_tuple[0]
            return self.game_object.move(self.my_id, current_best_move)
