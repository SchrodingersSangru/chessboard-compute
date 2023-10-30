import numpy as np
import matplotlib.pyplot as plt
import time

def create_chessboard():
    # Create an 8x8 chessboard pattern with black and white squares
    chessboard = np.zeros((8, 8), dtype=int)
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 1:
                chessboard[i][j] = 1
    return chessboard

def knight_moves(n, initial_position):
    # Initialize the chessboard, knight's position, and visit count
    chessboard = create_chessboard()
    row, col = initial_position
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]

    # Move the knight for n times
    for step in range(1, n + 1):
        chessboard[row][col] = step  # Update the visit count
        draw_chessboard(chessboard)
        time.sleep(1)  # Sleep for 1 second to show the simulation

        next_moves = []
        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8 and chessboard[new_row][new_col] == 0:
                next_moves.append((new_row, new_col))
        if next_moves:
            min_moves = float('inf')
            for move in next_moves:
                num_moves = sum(1 for dr, dc in moves if 0 <= row + dr < 8 and 0 <= col + dc < 8)
                if num_moves < min_moves:
                    min_moves = num_moves
                    row, col = move

def draw_chessboard(board):
    fig, ax = plt.subplots()
    ax.matshow(board, cmap='Blues')

    for i in range(8):
        for j in range(8):
            ax.text(j, i, str(board[i][j]), va='center', ha='center', fontsize=12, color='red')

    plt.show()

if __name__ == "__main__":
    # User-defined values
    n = 64  # Number of moves
    initial_position = (0, 0)  # Initial position, e.g., (0, 0) for a1

    knight_moves(n, initial_position)

