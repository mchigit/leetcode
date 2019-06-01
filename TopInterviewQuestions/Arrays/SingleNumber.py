"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Input: [4,1,2,1,2]
Output: 4


Idea: use bitwise XOR
N XOR N = 0. 0 XOR N = N
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0

        for num in nums:
            output ^= num

        return output