"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.


Solution:

1. A simple solution is just using a while loop and increment, but that is very slow if divisor is 1
2. We can use left shift instead, which is essentially multiplies by 2 every time. But things to note, need to find the remaining result
    hence the return multiplier + helper(dividend - result, divisor)
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1

        overFlowNeg = -2 ** 31
        overFlowPos = 2 ** 31 - 1

        result = self.helper(abs(dividend), abs(divisor))
        if result * sign >= overFlowPos:
            return overFlowPos
        if result * sign <= overFlowNeg:
            return overFlowNeg

        return result * sign

    def helper(self, dividend, divisor):
        if dividend < divisor or dividend == 0:
            return 0

        result = abs(divisor)
        multiplier = 1
        while result + result <= dividend:
            result += result
            multiplier += multiplier

        return multiplier + self.helper(dividend - result, divisor)