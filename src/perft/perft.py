import time

from src.data.states.board_states import BoardStates

from src.generator.move_generator import MoveGenerator

from src.constants.board_constants import MOVE_TYPES


class Perft:
    @staticmethod
    def get_time():
        return int(time.perf_counter() * 1000)

    @staticmethod
    def get_perft(app, depth):
        nodes = 0

        if depth == 0:
            return 1

        move_generator = MoveGenerator(app)
        moves = move_generator.get_moves()

        for move_count in range(moves.count):
            move = moves.moves[move_count]
            board_states = BoardStates.get_board_states(app.bitboard_manager)

            if not app.move_manager.make_move(move, MOVE_TYPES["all"]):
                continue

            nodes += Perft.get_perft(app, depth - 1)

            app.bitboard_manager.set_board_states(board_states)

        return nodes
