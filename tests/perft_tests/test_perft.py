import os
import sys

import json
import unittest

from pathlib import Path


def setup():
    directory_name = os.path.dirname(__file__)
    file_path = os.path.join(directory_name, "../..")
    absolute_path = os.path.abspath(file_path)

    sys.path.append(absolute_path)


setup()

from managers.move_manager import MoveManager
from managers.table_manager import TableManager
from managers.bitboard_manager import BitboardManager

from src.perft.perft import Perft


class TestPerft(unittest.TestCase):
    def setUp(self):
        self.table_manager = TableManager(self)
        self.bitboard_manager = BitboardManager(self)
        self.move_manager = MoveManager(self)

        data_path = Path(__file__).parent / "../data/perft/perft_data.json"

        with open(data_path, "r", encoding="utf-8") as file:
            self.perft_data = json.load(file)

    def test_perft_data(self):
        for data in self.perft_data:
            if data["depth"] > 3:
                continue

            self.bitboard_manager.parse_fen(data["fen"])
            nodes = Perft.get_perft(self, data["depth"])
            self.assertEqual(nodes, data["nodes"])


if __name__ == "__main__":
    unittest.main()
