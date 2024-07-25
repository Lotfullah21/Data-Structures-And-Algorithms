# Sudoku Solver:

<h2><a href="https://leetcode.com/problems/sudoku-solver/description/">Leetcode</a></h2>

## Approach

The approach used to solve the Sudoku puzzle is a classic Backtracking algorithm. Here’s a step-by-step breakdown of the approach:

## Initialization:

The solveSudoku function initializes the process and calls the helper function to start solving the puzzle.

## Backtracking:

The helper function iterates over each cell in the board.
If an empty cell (".") is found, it attempts to place each number from 1 to 9 in that cell.
For each number, the isValid function is called to check if placing that number is valid according to Sudoku rules.
If placing the number is valid, the number is placed, and a recursive call is made to attempt to solve the rest of the board.
If the recursive call returns True, the board is solved, and the function returns True.
If placing the number doesn't lead to a solution, the cell is reset to "." (backtracking).
If no number from 1 to 9 is valid, the function returns False, triggering further backtracking.

## Validity Check:

The isValid function checks whether placing a number in a specific cell is valid by:
Ensuring the number is not already present in the current row.
Ensuring the number is not already present in the current column.
Ensuring the number is not already present in the 3x3 sub-grid that the cell belongs to.

## Termination:

The helper function returns True if the entire board is filled correctly.
The recursion terminates once a solution is found, and the board is modified in place.
