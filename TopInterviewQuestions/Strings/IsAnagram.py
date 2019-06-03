"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
Well with Python, you don't have to. But let's say you are using Java, and you initilize an array of 26 because you need to hold 26 letters.
With unicode you need to increase array size.

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = {}
        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

        for letter in t:
            if letter not in letters:
                return False
            else:
                letters[letter] -= 1

        for letter in letters:
            if letters[letter] != 0:
                return False

        return True