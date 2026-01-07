import sys
import pygame
import random

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 25

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
COLORS = [RED, BLUE, GREEN]

# Tetromino shapes
SHAPES = [
    [
        [".....", ".....", ".....", "OOOO.", "....."],
        [".....", "..O..", "..O..", "..O..", "..O.."],
    ],
    [
        [".....", ".....", "..O..", ".OOO.", "....."],
        [".....", "..O..", ".OO..", "..O..", "....."],
        [".....", ".....", ".OOO.", "..O..", "....."],
        [".....", "..O..", "..OO.", "..O..", "....."],
    ],
    [
        [".....", ".....", "..OO.", ".OO..", "....."],
        [".....", ".....", ".OO..", "..OO.", "....."],
        [".....", ".O...", ".OO..", "..O..", "....."],
        [".....", "..O..", ".OO..", ".O...", "....."],
    ],
    [
        [".....", "..O..", "..O.", "..OO.", "....."],
        [".....", "...O.", ".OOO.", ".....", "....."],
        [".....", ".OO..", "..O..", "..O..", "....."],
        [".....", ".....", ".OOO.", ".O...", "....."],
    ],
]

class Tetromino:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(
            COLORS
        )  # You can choose different colors for each shape
        self.rotation = 0


class Tetris:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0  # Add score attribute

    def new_piece(self):
        # Choose a random shape
        shape = random.choice(SHAPES)
        # Return a new Tetromino object
        return Tetromino(self.width // 2, 0, shape)

    def valid_move(self, piece, x, y, rotation):
        """Check if the piece can move to the given position"""
        for i, row in enumerate(
            piece.shape[(piece.rotation + rotation) % len(piece.shape)]
        ):
            for j, cell in enumerate(row):
                try:
                    if cell == "O" and (
                        self.grid[piece.y + i + y][piece.x + j + x] != 0
                    ):
                        return False
                except IndexError:
                    return False
        return True

    def clear_lines(self):
        """Clear the lines that are full and return the number of cleared lines"""
        lines_cleared = 0
        for i, row in enumerate(self.grid[:-1]):
            if all(cell != 0 for cell in row):
                lines_cleared += 1
                del self.grid[i]
                self.grid.insert(0, [0 for _ in range(self.width)])
        return lines_cleared
