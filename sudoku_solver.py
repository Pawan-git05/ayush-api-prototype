#!/usr/bin/env python3
"""
Simple Sudoku Solver using Backtracking Algorithm

This module implements a sudoku solver that can solve standard 9x9 sudoku puzzles
using a backtracking algorithm.
"""

def print_board(board):
    """
    Pretty print the sudoku board with grid lines.
    
    Args:
        board (list): 9x9 list representing the sudoku board
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    """
    Find an empty cell (represented by 0) in the board.
    
    Args:
        board (list): 9x9 list representing the sudoku board
        
    Returns:
        tuple: (row, col) of empty cell, or None if board is full
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col
    
    return None


def is_valid(board, num, pos):
    """
    Check if a number is valid in the given position.
    
    Args:
        board (list): 9x9 list representing the sudoku board
        num (int): Number to check (1-9)
        pos (tuple): Position (row, col) to check
        
    Returns:
        bool: True if the number is valid, False otherwise
    """
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True


def solve(board):
    """
    Solve the sudoku puzzle using backtracking algorithm.
    
    Args:
        board (list): 9x9 list representing the sudoku board
        
    Returns:
        bool: True if puzzle is solved, False if no solution exists
    """
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def is_valid_board(board):
    """
    Check if the board is a valid sudoku puzzle format.
    
    Args:
        board (list): 9x9 list representing the sudoku board
        
    Returns:
        bool: True if board is valid format, False otherwise
    """
    if len(board) != 9:
        return False
    
    for row in board:
        if len(row) != 9:
            return False
        for cell in row:
            if not isinstance(cell, int) or cell < 0 or cell > 9:
                return False
    
    return True


def main():
    """Main function to demonstrate the sudoku solver."""
    
    # Example puzzle - replace 0s with your own puzzle
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print("Original Sudoku Puzzle:")
    print("=" * 25)
    print_board(puzzle)
    print("\n")
    
    if not is_valid_board(puzzle):
        print("Error: Invalid board format!")
        return
    
    if solve(puzzle):
        print("Solved Sudoku Puzzle:")
        print("=" * 25)
        print_board(puzzle)
    else:
        print("No solution exists for this puzzle!")


if __name__ == "__main__":
    main()
