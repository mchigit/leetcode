"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

from typing import List

"""
Runtime: 56 ms, faster than 88.28% of Python3 online submissions for Two Sum.
Memory Usage: 15.4 MB, less than 5.11% of Python3 online submissions for Two Sum.
"""
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 1:
            return []
        result = []
        numDict = {}
        for i in range(0, len(nums)):
            if nums[i] in numDict:
                result.append(numDict.get(nums[i]))
                result.append(i)
                break
            numDict[(target - nums[i])] = i

        return result

