# Constraint Satisfaction Problem using Backtracking
# N-Queens Problem

def print_board(board, n):

    for i in range(n):

        for j in range(n):

            if board[i] == j:
                print("Q", end=" ")

            else:
                print("_", end=" ")

        print()

    print()


# Check whether queen can be placed safely
def is_safe(board, row, col):

    for i in range(row):

        # Same column
        if board[i] == col:
            return False

        # Left diagonal
        if board[i] - i == col - row:
            return False

        # Right diagonal
        if board[i] + i == col + row:
            return False

    return True


# Backtracking function
def solve(board, row, n):

    # All queens placed
    if row == n:

        print("Solution Found:\n")

        print_board(board, n)

        return

    # Try every column
    for col in range(n):

        if is_safe(board, row, col):

            # Place queen
            board[row] = col

            # Recursive call
            solve(board, row + 1, n)

            # Backtrack
            board[row] = -1


# MAIN
n = 4

board = [-1] * n

print("Solving", n, "Queens Problem...\n")

solve(board, 0, n)