from src.parsers.move_parser import MoveParser

from src.constants.board_constants import MOVE_TYPES
from src.constants.parser_constants import INITIAL_BOARD


class CommandParser:
    def __init__(self, app):
        self.app = app
        self.index = 9

    def parse_position_command(self, command):
        self.parse_start_command(command)
        self.parse_moves_command(command)

        self.app.bitboard_manager.print_board()

    def parse_go_command(self, command):
        index = command.find("depth")

        if index == -1:
            return

        index += 6
        depth = int(command[index:])

    def parse_start_command(self, command):
        if "startpos" in command:
            self.app.bitboard_manager.parse_fen(INITIAL_BOARD)
            return

        self.parse_fen_command(command)

    def parse_fen_command(self, command):
        self.index = command.find("fen")

        if self.index == -1:
            self.app.bitboard_manager.parse_fen(INITIAL_BOARD)
            return

        self.index += 4
        fen_string = command[self.index :]

        self.app.bitboard_manager.parse_fen(fen_string)

    def parse_moves_command(self, command):
        self.index = command.find("moves")

        if self.index == -1:
            return

        move_strings = command[self.index :].split()

        self.parse_move_strings(move_strings)

    def parse_move_strings(self, move_strings):
        for move_string in move_strings:
            move_parser = MoveParser(self.app)
            move = move_parser.parse(move_string)

            if not move:
                continue

            self.app.move_manager.make_move(move, MOVE_TYPES["all"])
