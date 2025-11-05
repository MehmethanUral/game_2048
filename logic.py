import copy
import random

def start_game():

    mat = [[0] * 4 for _ in range(4)]

    add_new_2(mat)
    add_new_2(mat)
    
    return mat

def add_new_2(mat):

    empty_cells = []

    for r in range(4):
        for c in range(4):
            if mat[r][c] == 0:
                empty_cells.append((r,c))
            
    if empty_cells:
        r, c =random.choice(empty_cells)
        mat[r][c] = 2

def get_current_state(mat):

    for r in range(4):
        for c in range(4):
            if mat[r][c] == 2048:
                return 'WIN'
    
    for r in range(4):
        for c in range(4):
            if mat[r][c] == 0:
                return 'PLAY'
            
    for r in range(4):
        for c in range(3):
            if mat[r][c] == mat[r][c+1]:
                return 'PLAY'
            
    for r in range(3):
        for c in range(4):
            if mat[r][c] == mat[r+1][c]:
                return 'PLAY'
    return 'GAME OVER'   

def compress(mat):

    new_mat = [[0] *4 for _ in range(4)]

    for r in range(4):
        pos = 0
        for c in range(4):
            if mat[r][c] != 0:
                new_mat[r][pos] = mat[r][c]
                pos +=1
    return new_mat

def merge(mat):

    for r in range(4):
        for c in range(3):
            if mat[r][c] != 0 and mat[r][c] == mat[r][c+1]:
                mat[r][c] *= 2
                mat[r][c+1] = 0
    return mat

def reverse(mat):
    
    new_mat = []

    for row in mat:
        new_mat.append(row[::-1])
    return new_mat

def transpose(mat):

    new_mat = [[0] *4 for _ in range(4)]

    for r in range(4):
        for c in range(4):
            new_mat[c][r] = mat[r][c]
    return new_mat

def move_left(grid):

    grid = compress(grid)
    grid = merge(grid)
    grid = compress(grid)

    return grid

def move_right(grid):

    grid = reverse(grid)
    grid = move_left(grid)
    grid = reverse(grid)

    return grid

def move_up(grid):

    grid = transpose(grid)
    grid = move_left(grid)
    grid = transpose(grid)

    return grid

def move_down(grid):

    grid = transpose(grid)
    grid = move_right(grid)
    grid = transpose(grid)

    return grid