"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]


Idea:
The solution leverages a trick, which I probably would not think of during an actual interview:
To rotate the image, all you have to do is:
1) Flip the array based on the diagonal axis, in example 1 it would be [1, 5, 9]. So we get
  [1,4,7],
  [2,5,8],
  [3,6,9]
2) Then, flip based on middle axis:
    [7,4,1],
    [8,5,2],
    [9,6,3]

Else, rotate the array layer by layer
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            # why is it i + 1?
            for j in range(i + 1, len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(len(matrix)):
            for j in range(len(matrix[0]) // 2):
                # we only need to loop until the middle of the array to flip
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][len(matrix[0]) - 1 - j]
                matrix[i][len(matrix[0]) - 1 - j] = temp

