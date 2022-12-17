import random
import tkinter as tk

# Constantes du jeu
BLOCK_SIZE = 30
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
COLORS = ["purple", "cyan", "yellow", "orange", "blue", "red", "green"]
TETROMINO_SIZE = 4

class Tetromino:
    def __init__(self):
        self.x = 3
        self.y = 0
        self.shape = random.randint(1, 7)
        self.rotation = 0
        self.color = random.choice(COLORS)
        self.grid = create_tetromino_grid(self.shape, self.rotation)

def create_tetromino_grid(shape, rotation):
    grid = [[0 for _ in range(TETROMINO_SIZE)] for _ in range(TETROMINO_SIZE)]
    if shape == 1:
        if rotation == 0:
            grid[1][1] = 1
            grid[1][2] = 1
            grid[2][1] = 1
            grid[2][2] = 1
        elif rotation == 1:
            grid[1][1] = 1
            grid[1][2] = 1
            grid[2][1] = 1
            grid[2][2] = 1
        elif rotation == 2:
            grid[1][1] = 1
            grid[1][2] = 1
            grid[2][1] = 1
            grid[2][2] = 1
        elif rotation == 3:
            grid[1][1] = 1
            grid[1][2] = 1
            grid[2][1] = 1
            grid[2][2] = 1
    elif shape == 2:
        if rotation == 0:
            grid[1][2] = 1
            grid[2][2] = 1
            grid[3][2] = 1
            grid[4][2] = 1
        elif rotation == 1:
            grid[3][1] = 1
            grid[3][2] = 1
            grid[3][3] = 1
            grid[3][4] = 1
        elif rotation == 2:
            grid[1][1] = 1
            grid[2][1] = 1
            grid[3][1] = 1
            grid[4][1] = 1
        elif rotation == 3:
            grid[1][1] = 1
            grid[1][2] = 1
            grid[1][3] = 1
            grid[1][4] = 1
    elif shape == 3:
        if rotation == 0:
            grid[1][1] = 1
            grid[2][1] = 1
            grid[2][2] = 1
            grid[3][2] = 1
        elif rotation == 1:
            grid[2][3] = 1
            grid[3][3] = 1
            grid[3][2] = 1
            grid[3][1] = 1
        elif rotation == 2:
            grid[1][2] = 1
            grid[1][1] = 1
            grid[2][1] = 1
            grid[3][1] = 1
        elif rotation == 3:
            grid[1][1] = 1
            grid[2][1] = 1
            grid[2][2] = 1
            grid[3][2] = 1
    elif shape == 4:
        if rotation == 0:
            grid[1][2] = 1
            grid[2][2] = 1
            grid[2][1] = 1
            grid[3][1] = 1
        elif rotation == 1:
            grid[1][1] = 1
            grid[1][2] = 1
            grid[2][2] = 1
            grid[2][3] = 1
        elif rotation == 2:
            grid[1][2] = 1
            grid[1][3] = 1
            grid[2][1] = 1
            grid[2][2] = 1
        elif rotation == 3:
            grid[1][1] = 1
            grid[1][2] = 1
            grid[2][2] = 1
            grid[2][3] = 1
    elif shape == 5:
        if rotation == 0:
            grid[1][1] = 1
            grid[2][1] = 1
            grid[3][1] = 1
            grid[3][2] = 1
        elif rotation == 1:
            grid[1][1] = 1
            grid[1][2] = 1
            grid[1][3] = 1
            grid[2][3] = 1
        elif rotation == 2:
            grid[1][2] = 1
            grid[2][2] = 1
            grid[3][1] = 1
            grid[3][2] = 1
        elif rotation == 3:
            grid[2][1] = 1
            grid[2][2] = 1
            grid[2][3] = 1
            grid[1][3] = 1
    elif shape == 6:
        if rotation == 0 and (i, j) in [(1, 1), (1, 2), (2, 2), (3, 2)]:
            grid[1][1] = 1
            grid[1][2] = 1
            grid[2][2] = 1
            grid[3][2] = 1
        elif rotation == 1 and (i, j) in [(2, 1), (2, 2), (3, 2), (3, 3)]:
            grid[2][1] = 1
            grid[2][2] = 1
            grid[3][2] = 1
            grid[3][3] = 1
        elif rotation == 2 and (i, j) in [(1, 2), (2, 1), (2, 2), (2, 3)]:
            grid[1][2] = 1
            grid[2][1] = 1
            grid[2][2] = 1
            grid[2][3] = 1
        elif rotation == 3 and (i, j) in [(2, 2), (2, 3), (3, 3), (3, 4)]:
            grid[2][2] = 1
            grid[2][3] = 1
            grid[3][3] = 1
            grid[3][4] = 1
        elif shape == 7:
            if rotation == 0 and (i, j) in [(1, 1), (1, 2), (2, 2), (2, 3)]:
                grid[1][1] = 1
                grid[1][2] = 1
                grid[2][2] = 1
                grid[2][3] = 1
            elif rotation == 1 and (i, j) in [(1, 2), (2, 2), (2, 1), (3, 1)]:
                grid[1][2] = 1
                grid[2][2] = 1
                grid[2][1] = 1
                grid[3][1] = 1
            elif rotation == 2 and (i, j) in [(2, 1), (2, 2), (3, 2), (3, 3)]:
                grid[2][1] = 1
                grid[2][2] = 1
                grid[3][2] = 1
                grid[3][3] = 1
            elif rotation == 3 and (i, j) in [(2, 3), (2, 2), (1, 2), (1, 1)]:
                grid[2][3] = 1
                grid[2][2] = 1
                grid[1][2] = 1
                grid[1][1] = 1
        return grid

def rotate_tetromino(tetromino):
    tetromino.rotation = (tetromino.rotation + 1) % 4
    tetromino.grid = create_tetromino_grid(tetromino.shape, tetromino.rotation)
def move_tetromino(tetromino, board, dx, dy):
    tetromino.x += dx
    tetromino.y += dy

    if collides(tetromino, board):
        tetromino.x -= dx
        tetromino.y -= dy

def collides(tetromino, board):
    for i in range(TETROMINO_SIZE):
        for j in range(TETROMINO_SIZE):
            if tetromino.grid[i][j] == 1:
                if tetromino.x + j < 0 or tetromino.x + j >= BOARD_WIDTH or tetromino.y + i >= BOARD_HEIGHT or board[tetromino.y + i][tetromino.x + j] != 0:
                    return True
    return False

def create_board():
    return [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

def get_lines_to_clear(board):
    lines_to_clear = []
    for i in range(BOARD_HEIGHT):
        if all(board[i]):
            lines_to_clear.append(i)
    return lines_to_clear

def clear_lines(board, lines_to_clear):
    for line in lines_to_clear:
        board.pop(line)
        board.insert(0, [0 for _ in range(BOARD_WIDTH)])

def lock_tetromino(tetromino, board):
    for i in range(TETROMINO_SIZE):
        for j in range(TETROMINO_SIZE):
            if tetromino.grid[i][j] == 1:
                board[tetromino.y + i][tetromino.x + j] = tetromino.color

def draw_block(canvas, x, y, color):
    canvas.create_rectangle(x * BLOCK_SIZE, y * BLOCK_SIZE, (x + 1) * BLOCK_SIZE, (y + 1) * BLOCK_SIZE, fill=color, outline="black")

def draw_board(canvas, board):
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            if board[i][j] != 0:
                draw_block(canvas, j, i, board[i][j])

def draw_tetromino(canvas, tetromino):
    for i in range(TETROMINO_SIZE):
        for j in range(TETROMINO_SIZE):
            if tetromino.grid[i][j] == 1:
                draw_block(canvas, tetromino.x + j, tetromino.y + i, tetromino.color)
def draw_next_tetromino(canvas, tetromino):
    x = NEXT_TETROMINO_X
    y = NEXT_TETROMINO_Y
    for i in range(TETROMINO_SIZE):
        for j in range(TETROMINO_SIZE):
            if tetromino.grid[i][j] == 1:
                draw_block(canvas, x + j, y + i, tetromino.color)

def draw_score(canvas, score):
    canvas.create_text(SCORE_X, SCORE_Y, text=f"Score: {score}", font="Arial 20", anchor="w")

def draw(canvas, tetromino, next_tetromino, board, score):
    draw_board(canvas, board)
    draw_tetromino(canvas, tetromino)
    draw_next_tetromino(canvas, next_tetromino)
    draw_score(canvas, score)

def key_pressed(event, tetromino, board):
    if event.keysym == "Up":
        rotate_tetromino(tetromino)
        if collides(tetromino, board):
            rotate_tetromino(tetromino)
            rotate_tetromino(tetromino)
            rotate_tetromino(tetromino)
    elif event.keysym == "Left":
        move_tetromino(tetromino, board, -1, 0)
    elif event.keysym == "Right":
        move_tetromino(tetromino, board, 1, 0)
    elif event.keysym == "Down":
        move_tetromino(tetromino, board, 0, 1)

def main():
    root = tk.Tk()
    root.title("Tetris")
    root.resizable(False, False)

    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()

    tetromino = create_tetromino()
    next_tetromino = create_tetromino()
    board = create_board()

    score = 0
    level = 1
    speed = INITIAL_SPEED

def update():
