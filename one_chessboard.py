import numpy as np
import matplotlib.pyplot as plt

def is_valid_move(board, x, y, n):
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1

def knights_tour(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    moves_x = [2, 1, -1, -2, -2, -1, 1, 2]
    moves_y = [1, 2, 2, 1, -1, -2, -2, -1]
    x, y = 0, 0
    total_moves = n * n

    for move in range(1, total_moves):
        min_moves = float('inf')
        best_x, best_y = -1, -1

        for i in range(8):
            new_x, new_y = x + moves_x[i], y + moves_y[i]
            if is_valid_move(board, new_x, new_y, n):
                num_moves = 0
                for j in range(8):
                    next_x, next_y = new_x + moves_x[j], new_y + moves_y[j]
                    if is_valid_move(board, next_x, next_y, n):
                        num_moves += 1

                if num_moves < min_moves:
                    min_moves = num_moves
                    best_x, best_y = new_x, new_y

        x, y = best_x, best_y
        board[x][y] = move

    # Create a chessboard visualization
    fig, ax = plt.subplots()
    ax.matshow(np.ones((n, n)), cmap='Blues', extent=[0, n, 0, n])
    
    for i in range(n):
        for j in range(n):
            ax.text(j + 0.5, n - i - 0.5, str(board[i][j]), va='center', ha='center', fontsize=12, color='red')

    plt.show()

if __name__ == "__main__":
    n = int(input("Enter the size of the chessboard (n x n): "))
    if n < 8:
        print("Please choose a board size of 8x8 or larger.")
    else:
        knights_tour(n)
