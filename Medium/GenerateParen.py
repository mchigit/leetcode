"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

Using recursion - Backtracking

"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        result = []

        self.helper(n, n, "", result)

        return result

    def helper(self, left, right, current, result):
        if left > right:
            # we are checking whether the remaining left paren is greater than right paren
            # We check this because all the incorrect parenthesis formations at any stage
            # has more right paren than left paren
            return

        if left == 0 and right == 0:
            result.append(current)

        if left > 0:
            self.helper(left - 1, right, current + "(", result)
        if right > 0:
            self.helper(left, right - 1, current + ")", result)