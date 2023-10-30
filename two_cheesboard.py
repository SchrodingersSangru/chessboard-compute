import numpy as np
import matplotlib.pyplot as plt

def is_valid_move(board, x, y, n):
    return 0 <= x < n and 0 <= y < n and board[x][y] == 0

def knights_tour(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    moves_x = [2, 1, -1, -2, -2, -1, 1, 2]
    moves_y = [1, 2, 2, 1, -1, -2, -2, -1]
    x, y = 7, 2
    total_moves = n * n

    for move in range(1, total_moves + 1):
        board[x][y] = move
        available_moves = []

        for i in range(8):
            new_x, new_y = x + moves_x[i], y + moves_y[i]
            if is_valid_move(board, new_x, new_y, n):
                num_moves = 0
                for j in range(8):
                    next_x, next_y = new_x + moves_x[j], new_y + moves_y[j]
                    if is_valid_move(board, next_x, next_y, n):
                        num_moves += 1

                available_moves.append((num_moves, i))

        if not available_moves:
            break

        available_moves.sort()
        min_moves, best_move = available_moves[0]
        x, y = x + moves_x[best_move], y + moves_y[best_move]

    # Create a chessboard visualization
    fig, ax = plt.subplots()
    ax.matshow(np.ones((n, n)), cmap='Blues', extent=[0, n, 0, n])
    
    for i in range(n):
        for j in range(n):
            ax.text(j + 0.5, n - i - 0.5, str(board[i][j]), va='center', ha='center', fontsize=12, color='red')

    plt.show()

if __name__ == "__main__":
    n = int(input("Enter the size of the chessboard (n x n): "))
    if n < 5:
        print("Please choose a board size of at least 5x5.")
    else:
        knights_tour(n)
