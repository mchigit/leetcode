"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.


Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

Solution:

Notice a pattern: the largest the distance (Horizontal axis), the higher the volume
Also notice: the height of the container is defined by the shorter one
So, we can have 2 pointers from start to finish, keeping track of largest volume
Move the pointer that has the smaller height

"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        start, end = 0, len(height) - 1
        while start < end:
            area = (end - start) * min(height[end], height[start])
            if area > maxArea:
                maxArea = area

            if height[end] < height[start]:
                end -= 1
            else:
                start += 1

        return maxArea