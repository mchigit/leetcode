"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.


Solution:

We have to loop through the matrix either way. We create 3 dictionaries for every row in the matrix:
1) check if row dictionaries contains current number
2) check if column dictionaries contains current number
3) check if cube dictionaries contains current number

The difficulty in this question is how do you check if the cube dictionaries contains current number
"""
from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
    for i in range(len(board)):
        rowDict = {}
        colDict = {}
        cubeDict = {}
        for j in range(len(board)):
            if board[i][j] != "." and board[i][j] in rowDict:
                return False
            else:
                rowDict[board[i][j]] = board[i][j]
            if board[j][i] != "." and board[j][i] in colDict:
                return False
            else:
                colDict[board[j][i]] = board[j][i]

            # check if the current number is in the cube dictionary
            # Why does this work?
            rowIndex = 3 * (i // 3)
            colIndex = 3 * (i % 3)

            if board[rowIndex + j // 3][colIndex + j % 3] != "." and board[rowIndex + j // 3][colIndex + j % 3] in cubeDict:
                return False
            else:
                cubeDict[board[rowIndex + j // 3][colIndex + j % 3]] = board[rowIndex + j // 3][colIndex + j % 3]

    return True


if __name__ == "__main__":
    sudoku = [[".",".",".",".","5",".",".","1","."],
              [".","4",".","3",".",".",".",".","."],
              [".",".",".",".",".","3",".",".","1"],
              ["8",".",".",".",".",".",".","2","."],
              [".",".","2",".","7",".",".",".","."],
              [".","1","5",".",".",".",".",".","."],
              [".",".",".",".",".","2",".",".","."],
              [".","2",".","9",".",".",".",".","."],
              [".",".","4",".",".",".",".",".","."]]
    print(isValidSudoku(sudoku))