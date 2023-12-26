from src.constants.board_constants import SQUARES

SIDES = {
    "white": 0,
    "black": 1,
    "all": 2,
}

SLIDERS = {
    "rook": 0,
    "bishop": 1,
}

CASTLE = {
    "K": 1,
    "Q": 2,
    "k": 4,
    "q": 8,
}

PIECES = {
    "P": 0,
    "N": 1,
    "B": 2,
    "R": 3,
    "Q": 4,
    "K": 5,
    "p": 6,
    "n": 7,
    "b": 8,
    "r": 9,
    "q": 10,
    "k": 11,
}

PROMOTION_PIECES = {
    PIECES["Q"]: "q",
    PIECES["R"]: "r",
    PIECES["B"]: "b",
    PIECES["N"]: "n",
    PIECES["q"]: "q",
    PIECES["r"]: "r",
    PIECES["b"]: "b",
    PIECES["n"]: "n",
}

ASCII_PIECES = "PNBRQKpnbrqk"
UNICODE_PIECES = "♙♘♗♖♕♔♟♞♝♜♛♚"

KING_SIDE_SQUARES = [
    (SQUARES["f1"], SQUARES["g1"]),
    (SQUARES["f8"], SQUARES["g8"]),
]

QUEEN_SIDE_SQUARES = [
    (SQUARES["b1"], SQUARES["c1"], SQUARES["d1"]),
    (SQUARES["b8"], SQUARES["c8"], SQUARES["d8"]),
]

KING_ATTACKED_SQUARES = [
    (SQUARES["e1"], SQUARES["f1"]),
    (SQUARES["e8"], SQUARES["f8"]),
]

QUEEN_ATTACKED_SQUARES = [
    (SQUARES["e1"], SQUARES["d1"]),
    (SQUARES["e8"], SQUARES["d8"]),
]
