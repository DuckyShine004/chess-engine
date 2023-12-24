from dataclasses import dataclass


@dataclass
class MoveParameters:
    source: int
    target: int
    piece: int
    promoted: int
    capture: int
    double: int
    enpassant: int
    castling: int
