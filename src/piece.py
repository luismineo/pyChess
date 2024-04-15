import math
import os


class Piece:
    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self, size):
        self.texture = os.path.join(
            f'assests/images/imgs-{size}px/{self.color}_{self.name}-export.png'
        )

    def add_moves(self, move):
        self.moves.append(move)


class Pawn(Piece):
    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1
        super().__init__('pawn', color, 1.0)


class Knight(Piece):
    def __init__(self, color):
        super().__init__('knight', color, 3.0)


class Bishop(Piece):
    def __init__(self, color):
        super().__init__('bishop', color, 3.0)


class Rook(Piece):
    def __init__(self, color):
        super().__init__('rook', color, 5.0)


class Queen(Piece):
    def __init__(self, color):
        super().__init__('queen', color, 9.0)


class King(Piece):
    def __init__(self, color):
        super().__init__('king', color, math.inf)
        # self.castle = True
        # self.check = False
        # self.checkmate = False
        # self.stalemate = False
        # self.in_check = False
        # self.in_checkmate = False
        # self.in_stalemate = False
        # self.in_draw = False