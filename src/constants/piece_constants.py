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

PROMOTED_PIECES = {
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
