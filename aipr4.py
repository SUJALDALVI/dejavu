# N-Queens Problem using Backtracking
# Constraint Satisfaction Problem (CSP)

def print_board(board, n):

    for i in range(n):

        for j in range(n):

            if board[i] == j:
                print("Q", end=" ")

            else:
                print("_", end=" ")

        print()

    print()


# check whether queen can be placed
def is_safe(board, row, col):

    for i in range(row):

        # same column
        if board[i] == col:
            return False

        # left diagonal
        if board[i] - i == col - row:
            return False

        # right diagonal
        if board[i] + i == col + row:
            return False

    return True


# solve function
def solve(board, row, n):

    # all queens placed
    if row == n:

        print("Solution Found:\n")

        print_board(board, n)

        return

    # try every column
    for col in range(n):

        if is_safe(board, row, col):

            # place queen
            board[row] = col

            # go to next row
            solve(board, row + 1, n)

            # remove queen (backtrack)
            board[row] = -1


# MAIN
n = 4

board = [-1] * n

print("Solving", n, "Queens Problem...\n")

solve(board, 0, n)