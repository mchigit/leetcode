"""
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Notes:

1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1
"""

from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            self.swapAndInvert(A[i])
        return A

    def swapAndInvert(self, L: List[int]) -> List[int]:
        endIndex = len(L) // 2
        for i in range(endIndex):
            temp = self.invert(L[i])
            L[i] = self.invert(L[len(L) - i - 1])
            L[len(L) - i - 1] = temp
        if len(L) % 2 == 1:
            # length of the array is odd, invert middle element
            L[len(L) // 2] = self.invert(L[len(L) // 2])
        return L

    def invert(self, num: int) -> int:
        if num == 1:
            return 0
        return 1



if __name__ == '__main__':
    matrix = [[1,1,0],[1,0,1],[0,0,0]]
    print(Solution().flipAndInvertImage(matrix))
