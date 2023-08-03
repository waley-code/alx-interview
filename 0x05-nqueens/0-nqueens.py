#!/usr/bin/python
import sys

def is_safe(board, row, col, N):
    """
    Check if placing a queen at a specific position on the board is safe.

    Args:
        board (list): The current state of the board represented as a list.
        row (int): The row index of the position to check.
        col (int): The column index of the position to check.
        N (int): The size of the board.

    Returns:
        bool: True if placing a queen at the position is safe, False otherwise.
    """
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens(N, board, row, result):
    """
    Recursive function to find all possible solutions to the N Queens problem.

    Args:
        N (int): The size of the board.
        board (list): The current state of the board represented as a list.
        row (int): The current row being processed.
        result (list): A list to store the found solutions.
    """
    if row == N:
        result.append([[i, board[i]] for i in range(N)])
    else:
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                solve_nqueens(N, board, row + 1, result)

def print_nqueens_solutions(N):
    """
    Main function to print all possible solutions to the N Queens problem.

    Args:
        N (int): The size of the board.

    Prints:
        list: Prints each possible solution, where each solution is a list of coordinates
              representing the positions of the queens on the board.
    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    result = []

    solve_nqueens(N, board, 0, result)

    for solution in result:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        print_nqueens_solutions(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
