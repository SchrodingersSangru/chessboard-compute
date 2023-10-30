import numpy as np
import matplotlib.pyplot as plt

# Initialize the chessboard
n = 8  # Size of the chessboard (8x8)
chessboard = np.zeros((n, n), dtype=int)

# Possible moves for the knight
moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
         (-2, -1), (-1, -2), (1, -2), (2, -1)]

def is_valid_move(x, y):
    return 0 <= x < n and 0 <= y < n and chessboard[x][y] == 0

def knight_tour(x, y, move_number):
    if move_number == 64:
        return True

    for move in moves:
        new_x, new_y = x + move[0], y + move[1]
        if is_valid_move(new_x, new_y):
            chessboard[new_x][new_y] = move_number + 1
            if knight_tour(new_x, new_y, move_number + 1):
                return True
            chessboard[new_x][new_y] = 0  # Backtrack

    return False

# Start the knight's tour from position (0, 0)
start_x, start_y = 7, 4
chessboard[start_x][start_y] = 1

# Perform the knight's tour
if knight_tour(start_x, start_y, 1):
    print("Knight's Tour Completed:")
    print(chessboard)
else:
    print("No Solution Found")

# Visualization
fig, ax = plt.subplots()
ax.matshow(chessboard, cmap='Blues')
for i in range(n):
    for j in range(n):
        ax.text(j, i, str(chessboard[i][j]), va='center', ha='center', fontsize=12, color='red')

plt.show()
