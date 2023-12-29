from src.parsers.move_parser import MoveParser

from src.constants.board_constants import MOVE_TYPES
from src.constants.parser_constants import INITIAL_BOARD


class PositionParser:
    def __init__(self, app):
        self.app = app

    def parse(self, command):
        # We start reading the command string at index 9
        index = 9

        # parse startpos command
        if "startpos" in command[index:]:
            # Initialize chess board with start position
            self.app.bitboard_manager.parse_fen(INITIAL_BOARD)

        # Otherwise
        else:
            # Make sure that the fen command is available within the command string
            index = command.find("fen")

            if index == -1:
                self.app.bitboard_manager.parse_fen(INITIAL_BOARD)

            # If we did find the fen command, then we shift the pointer again to get the fen string
            else:
                index += 4

                # Initialize position from fen string
                self.app.bitboard_manager.parse_fen(command[index:])

        # Parse moves after position
        index = command.find("moves")

        if index != -1:
            index += 6

            # Parse the move strings
            move_strings = command[index:].split(" ")

            for move_string in move_strings:
                move_parser = MoveParser(self.app)
                move = move_parser.parse(move_string)

                # If the current move is not valid, then we skip it
                if not move:
                    continue

                self.app.move_manager.make_move(move, MOVE_TYPES["all"])
