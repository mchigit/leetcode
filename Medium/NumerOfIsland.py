"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

Solution:

Loop through the matrix, if encounter 1, add to island count
Then write a recursive method to turn all near by 1 to 0
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == None:
            return 0

        islandCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islandCount += 1
                    self.convertOneToZero(grid, i, j)

        return islandCount

    def convertOneToZero(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
            return

        grid[i][j] = "0"
        self.convertOneToZero(grid, i, j + 1)
        self.convertOneToZero(grid, i, j - 1)
        self.convertOneToZero(grid, i + 1, j)
        self.convertOneToZero(grid, i - 1, j)
