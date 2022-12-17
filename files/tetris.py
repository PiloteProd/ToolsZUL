import tkinter as tk
import random

# Constantes pour la taille de la grille et la taille des blocs
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 30

# Constantes pour les couleurs des différentes formes de Tetris
COLORS = ['cyan', 'blue', 'orange', 'yellow', 'green', 'purple', 'red']

# Classe qui représente une forme de Tetris
class Tetromino:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = COLORS[shape]
        self.rotation = 0

# Fonction qui crée une nouvelle forme de Tetris aléatoire
def new_tetromino():
    shape = random.randint(0, 6)
    tetromino = Tetromino(5, 0, shape)
    return tetromino

# Fonction qui dessine une forme de Tetris dans le canvas
def draw_tetromino(canvas, tetromino):
    for i in range(4):
        for j in range(4):
            if tetromino.shape == 0:
                if tetromino.rotation == 0 and (i, j) in [(1, 2), (2, 2), (3, 2), (2, 3)]:
                    canvas.create_rectangle(tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE,
                                           tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE + BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE + BLOCK_SIZE,
                                           fill=tetromino.color)
                elif tetromino.rotation == 1 and (i, j) in [(2, 1), (1, 2), (2, 2), (3, 2)]:
                    canvas.create_rectangle(tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE,
                                           tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE + BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE + BLOCK_SIZE,
                                           fill=tetromino.color)
                elif tetromino.rotation == 2 and (i, j) in [(2, 1), (1, 2), (2, 2), (3, 2)]:
                    canvas.create_rectangle(tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE,
                                            tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE,
                                            tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE + BLOCK_SIZE,
                                            tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE + BLOCK_SIZE,
                                            fill=tetromino.color)
                elif tetromino.rotation == 3 and (i, j) in [(2, 2), (1, 3), (2, 3), (3, 3)]:
                    canvas.create_rectangle(tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE,
                                            tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE,
                                            tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE + BLOCK_SIZE,
                                            tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE + BLOCK_SIZE,
                                            fill=tetromino.color)
                elif tetromino.shape == 1:
                    if tetromino.rotation == 0 and (i, j) in [(1, 2), (2, 2), (2, 3), (3, 3)]:
                        canvas.create_rectangle(tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE,
                                                tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE,
                                                tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE + BLOCK_SIZE,
                                                tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE + BLOCK_SIZE,
                                                fill=tetromino.color)
                    elif tetromino.rotation == 1 and (i, j) in [(2, 2), (2, 1), (1, 3), (2, 3)]:
                        canvas.create_rectangle(tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE,
                                                tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE,
                                                tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE + BLOCK_SIZE,
                                                tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE + BLOCK_SIZE,
                                                fill=tetromino.color)
                    elif tetromino.rotation == 2 and (i, j) in [(1, 2), (2, 2), (2, 1), (3, 1)]:
                        canvas.create_rectangle(tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE,
                                                tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE,
                                                tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE + BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE + BLOCK_SIZE,
                                           fill=tetromino.color)
                elif tetromino.rotation == 3 and (i, j) in [(1, 1), (2, 1), (2, 2), (2, 3)]:
                    canvas.create_rectangle(tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE,
                                           tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE + BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE + BLOCK_SIZE,
                                           fill=tetromino.color)
            elif tetromino.shape == 2:
                if tetromino.rotation == 0 and (i, j) in [(1, 1), (2, 1), (2, 2), (3, 2)]:
                    canvas.create_rectangle(tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE,
                                           tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE + BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE + BLOCK_SIZE,
                                           fill=tetromino.color)
                elif tetromino.rotation == 1 and (i, j) in [(2, 1), (2, 2), (1, 2), (1, 3)]:
                    canvas.create_rectangle(tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE,
                                           tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE + BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE + BLOCK_SIZE,
                                           fill=tetromino.color)
                elif tetromino.rotation == 2 and (i, j) in [(1, 2), (2, 2), (2, 1), (3, 1)]:
                    canvas.create_rectangle(tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE,
                                           tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE + BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE + BLOCK_SIZE,
                                           fill=tetromino.color)
                elif tetromino.rotation == 3 and (i, j) in [(2, 3), (2, 2), (1, 2), (1, 1)]:
                    canvas.create_rectangle(tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE + BLOCK_SIZE,
                                           fill=tetromino.color)
            elif tetromino.shape == 3:
                if tetromino.rotation == 0 and (i, j) in [(1, 1), (2, 1), (3, 1), (3, 2)]:
                    canvas.create_rectangle(tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE,
                                           tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE + BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE + BLOCK_SIZE,
                                           fill=tetromino.color)
                elif tetromino.rotation == 1 and (i, j) in [(2, 1), (2, 2), (2, 3), (1, 3)]:
                    canvas.create_rectangle(tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE,
                                           tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE + BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE + BLOCK_SIZE,
                                           fill=tetromino.color)
                elif tetromino.rotation == 2 and (i, j) in [(1, 2), (2, 2), (3, 2), (1, 1)]:
                    canvas.create_rectangle(tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE,
                                           tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE + BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE + BLOCK_SIZE,
                                           fill=tetromino.color)
                elif tetromino.rotation == 3 and (i, j) in [(2, 3), (2, 2), (2, 1), (3, 1)]:
                    canvas.create_rectangle(tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE,
                                           tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE + BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE + BLOCK_SIZE,
                                           fill=tetromino.color)
            elif tetromino.shape == 4:
                if tetromino.rotation == 0 and (i, j) in [(1, 2), (2, 2), (2, 1), (3, 1)]:
                    canvas.create_rectangle(tetromino.x * BLOCK_SIZE + j * BLOCK_SIZE, tetromino.y * BLOCK_SIZE + i * BLOCK_SIZE + BLOCK_SIZE,
                                           fill=tetromino.color)