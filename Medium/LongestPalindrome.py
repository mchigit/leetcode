"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"


Solution:
Given a letter in the string, we can expand to left and right at the same time
If they are the same, then the string is a palindrome:
a - palindrome
bab - palindrome since b = b
cbabs - not palindrome since c != s

This works for bab, since we can just use a as starting letter, but doesn't work for bb. We need to pass 2 letters for expanding

So we just loop through every single letter in the string, and expand until we find the longest palindrome
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ""

        for i in range(len(s)):
            # check case 1, pass 1 letter in, and expand
            longestPalindrome = self.getLongestPalindrome(s, i, i)
            if len(longestPalindrome) > len(palindrome):
                palindrome = longestPalindrome

            # check case 2, pass 2 letters in, and expand
            longest2 = self.getLongestPalindrome(s, i, i + 1)
            if len(longest2) > len(palindrome):
                palindrome = longest2

        return palindrome

    def getLongestPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1: right]