"""
Check if array has duplicates. Pretty simple. 
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = {}
        for num in nums:
            if num in unique:
                return True
            else:
                unique[num] = True

        return False