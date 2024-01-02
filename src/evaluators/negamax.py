from src.data.states.board_states import BoardStates

from src.routines.attacked import Attacked

from src.generator.move_generator import MoveGenerator

from src.utilities.bit import Bit
from src.utilities.console import Console

from src.evaluators.rudimentary import Rudimentary

from src.constants.piece_constants import SIDES, PIECES
from src.constants.board_constants import MOVE_TYPES


class Negamax:
    overall_best_move = None
    ply = 0

    @staticmethod
    def evaluate(app, alpha, beta, depth):
        nodes = 0

        if depth == 0:
            return Rudimentary.get_evaluation(app)

        nodes += 1

        legal_moves = 0
        square = (
            Bit.get_least_significant_first_bit(app.bitboard_manager.bitboards[PIECES["K"]])
            if app.bitboard_manager.side == SIDES["white"]
            else Bit.get_least_significant_first_bit(app.bitboard_manager.bitboards[PIECES["k"]])
        )
        is_king_in_check = Attacked.check_squares_attacked(app, square, app.bitboard_manager.side ^ 1)

        old_alpha = alpha
        current_best_move = None

        move_generator = MoveGenerator(app)
        moves = move_generator.get_moves()

        for move_count in range(moves.count):
            move = moves.moves[move_count]
            board_states = BoardStates.get_board_states(app.bitboard_manager)

            Negamax.ply += 1

            if app.move_manager.make_move(move, MOVE_TYPES["all"]) == 0:
                Negamax.ply -= 1
                continue

            legal_moves += 1

            score = -Negamax.evaluate(app, -beta, -alpha, depth - 1)

            Negamax.ply -= 1

            app.bitboard_manager.set_board_states(board_states)

            if score >= beta:
                return beta

            if score > alpha:
                alpha = score

                if Negamax.ply == 0:
                    current_best_move = moves.moves[move_count]

        if legal_moves == 0:
            # King is in check
            if is_king_in_check:
                return -49000 + Negamax.ply

            # King is not in check -> stalemate
            return 0

        if old_alpha != alpha:
            Negamax.overall_best_move = current_best_move

        return alpha

    @staticmethod
    def search(app, depth):
        score = Negamax.evaluate(app, -50000, 50000, depth)
        Console.print_move(Negamax.overall_best_move)

        app.move_manager.make_move(Negamax.overall_best_move, MOVE_TYPES["all"])
        app.bitboard_manager.print_board()
