"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

This solution is not the most efficient out of leetcode submissions. But other submission leverages Python built-in functions

"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        letterDict = {}

        for i in range(len(s)):
            if s[i] in letterDict:
                letterDict[s[i]] += 1
            else:
                letterDict[s[i]] = 1

        for i in range(len(s)):
            if letterDict[s[i]] == 1:
                return i

        return -1