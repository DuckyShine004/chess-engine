class Moves:
    def __init__(self):
        self.moves = [0] * 256
        self.count = 0

    def add_move(self, move):
        print(self.count)
        self.moves[self.count] = move
        self.count += 1
