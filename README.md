# Sudoku Solver

A simple sudoku solver implemented in Python that uses backtracking algorithm to solve 9x9 sudoku puzzles.

## Features

- Solves standard 9x9 sudoku puzzles
- Uses backtracking algorithm for efficient solving
- Validates puzzle input and solution
- Pretty prints the solved puzzle

## Usage

```python
python sudoku_solver.py
```

The solver will run with the example puzzle included in the code. To solve your own puzzle, modify the `puzzle` variable in the `sudoku_solver.py` file.

## Puzzle Format

Puzzles should be represented as a 9x9 list of lists, where:
- Empty cells are represented by 0
- Numbers 1-9 represent the given clues

Example:
```python
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
```
