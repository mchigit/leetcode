"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


Idea: use dict to keep track of number of occurances

Follow up:

1) if already sorted, just have 2 pointers to loop through the array
2) If 2 arrays are sorted, then using binary search is actually faster. For each element in num1, search in num2. O(nlogm) which is faster than O(n + m)
3)

"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output, hashStore = [], {}

        for num in nums1:
            if num in hashStore:
                hashStore[num] += 1
            else:
                hashStore[num] = 1

        for num in nums2:
            if num in hashStore and hashStore[num] > 0:
                output.append(num)
                hashStore[num] -= 1

        return output

    def intersectFollowUp(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        pointer1, pointer2 = 0, 0
        while pointer1 < len(nums1) and pointer2 < len(nums2):
            if nums1[pointer1] == nums2[pointer2]:
                output.append(nums1[pointer1])
                pointer1 += 1
                pointer2 += 1
            elif nums1[pointer1] > nums2[pointer2]:
                pointer2 += 1
            else:
                pointer1 += 1


        return output
