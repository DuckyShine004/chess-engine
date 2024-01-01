from src.data.states.board_states import BoardStates

from src.generator.move_generator import MoveGenerator

from src.utilities.console import Console

from src.evaluators.rudimentary import Rudimentary

from src.constants.board_constants import MOVE_TYPES


class Negamax:
    overall_best_move = None

    @staticmethod
    def evaluate(app, alpha, beta, depth):
        ply = 0
        nodes = 0

        if depth == 0:
            return Rudimentary.get_evaluation(app)

        nodes += 1

        old_alpha = alpha
        current_best_move = None

        move_generator = MoveGenerator(app)
        moves = move_generator.get_moves()

        for move_count in range(moves.count):
            move = moves.moves[move_count]
            board_states = BoardStates.get_board_states(app.bitboard_manager)

            ply += 1

            if not app.move_manager.make_move(move, MOVE_TYPES["all"]):
                ply -= 1
                continue

            score = -Negamax.evaluate(app, -beta, -alpha, depth - 1)

            ply -= 1

            app.bitboard_manager.set_board_states(board_states)

            if score >= beta:
                return beta

            if score > alpha:
                alpha = score

                if ply == 0:
                    current_best_move = moves.moves[move_count]

        if old_alpha != alpha:
            Negamax.overall_best_move = current_best_move

        return alpha

    @staticmethod
    def search(app, depth):
        score = Negamax.evaluate(app, -50000, 50000, depth)
        Console.print_move(Negamax.overall_best_move)

        app.move_manager.make_move(Negamax.overall_best_move, MOVE_TYPES["all"])
        app.bitboard_manager.print_board()
