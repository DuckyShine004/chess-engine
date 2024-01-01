import getch, chess
from src.data.states.board_states import BoardStates

from managers.table_manager import TableManager
from managers.bitboard_manager import BitboardManager
from managers.move_manager import MoveManager

from src.data.parameters.move_parameters import MoveParameters
from src.data_structures.moves import Moves

from src.routines.codec import Codec

from src.perft.perft import Perft

from src.evaluators.rudimentary import Rudimentary
from src.evaluators.negamax import Negamax

from src.utilities.bit import Bit
from src.utilities.attack import Attack
from src.utilities.console import Console

from src.parsers.move_parser import MoveParser
from src.parsers.command_parser import CommandParser

from src.generator.move_generator import MoveGenerator

from src.constants.piece_constants import PIECES, SIDES, UNICODE_PIECES
from src.constants.board_constants import SQUARES, COORDINATES, MOVE_TYPES
from src.constants.parser_constants import (
    EMPTY_BOARD,
    TRICKY_BOARD,
    DEBUG_BOARD,
    KILLER_BOARD,
    INITIAL_BOARD,
)


class App:
    def __init__(self):
        self.table_manager = TableManager(self)
        self.bitboard_manager = BitboardManager(self)
        self.move_manager = MoveManager(self)

        print("Tables initialized")
        self.bitboard_manager.parse_fen(INITIAL_BOARD)
        self.bitboard_manager.print_board()

        self.command_parser = CommandParser(self)
        self.running = False

    def start_uci(self):
        self.running = True

        while self.running:
            command = input()
            self.handle_uci_commands(command)

    def handle_uci_commands(self, command):
        commands = command.split()

        match commands[0]:
            case "isready":
                print("readyok")
            case "ucinewgame":
                self.command_parser.parse_position_command("position startpos")
            case "position":
                self.command_parser.parse_position_command(command)
            case "go":
                self.command_parser.parse_go_command(command)
            case "quit":
                self.running = False
            case _:
                print("command is not recognized")
