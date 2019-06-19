"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Solution:

You are essentially using BFS. But the question is why is this more efficient than nested for loops?
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        output = []
        if not digits:
            return output

        self.getLetterCombination(output, "", digits, 0, phone)

        return output

    def getLetterCombination(self, result, combination, digits, current, phone):
        if current == len(digits):
            result.append(combination)
        else:
            for letter in phone[digits[current]]:
                self.getLetterCombination(result, combination + letter, digits, current + 1, phone)