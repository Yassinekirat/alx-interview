#!/usr/bin/python3
"""N Queens"""
import sys


def Nqueens(N):
    """creating the board"""
    board = [[0 for i in range(N)] for i in range(N)]
    solutions = []

    if not Nqueens_helper(board, 0, solutions):
        print("No solution")

    print_solutions(solutions)


def Nqueens_helper(board, col, solutions):
    """N queens helper"""
    if col >= len(board):
        solutions.append([[i, board[i].index(1)] for i in range(len(board))])
        return True

    res = False
    for i in range(len(board)):
        if SafeQueen(board, i, col):
            board[i][col] = 1

            res = Nqueens_helper(board, col + 1, solutions) or res

            board[i][col] = 0

    return res


def SafeQueen(board, row, col):
    """check if safe"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def print_solutions(solutions):
    """print solution"""
    for solution in solutions:
        print(solution)


def main():
    """main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    Nqueens(N)


if __name__ == "__main__":
    main()
