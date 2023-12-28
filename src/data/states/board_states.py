from typing import List

from dataclasses import dataclass


@dataclass
class BoardStates:
    bitboards: List[int]
    occupancies: List[int]
    side: int
    enpassant: int
    castle: int

    @staticmethod
    def get_board_states(manager):
        return BoardStates(
            bitboards=list(manager.bitboards),
            occupancies=list(manager.occupancies),
            side=manager.side,
            enpassant=manager.enpassant,
            castle=manager.castle,
        )
