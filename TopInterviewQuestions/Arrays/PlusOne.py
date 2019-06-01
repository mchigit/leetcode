"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Many different solutions exist

1) Convert the array into a number, add 1 then convert back into an array. This method requires looping through the array twice. But O(2n) = O(n)
2) Loop from end to start, if number is 9, put it as 0. If not, put it as self += 1. Then check after the loop whether first element is 0. If it is, insert 1 at the beginning
    This solution uses more memory than previous solution based on Leetcode

"""
from typing import List


class Solution:
    def plusOne1(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits)-1-i))
        return [int(i) for i in str(num+1)]

    def plusOne2(self, digits: List[int]):
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        if  digits[0] == 0:
            digits.insert(0, 1)
        return digits

