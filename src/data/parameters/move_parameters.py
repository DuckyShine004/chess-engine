from dataclasses import dataclass


@dataclass
class MoveParameters:
    source_square: int
    target_square: int
    piece: int
    promoted_piece: int
    capture_flag: int
    double_pawn_push_flag: int
    enpassant_flag: int
    castling_flag: int
