"""
  Implement strStr()
  Go to Discuss
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Solution:

Loop through string and compare

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            hasMatch = True
            haystackIndex = i
            for j in range(len(needle)):
                if haystack[haystackIndex] != needle[j]:
                    hasMatch = False
                    break
                else:
                    haystackIndex += 1

            if hasMatch:
                return i

        return -1

