"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

Solution:

1) Obviously you can just have a stack, append then pop to check the reverse. But this requires looping through string twice
2) Have 2 pointers, from start and end. Skip through any punctuations, then starts comparing. For a palindrome, letters should be same going forward and backward.
"""

def isPalindrome(s: str) -> bool:
    lettersStack = []
    for letter in s:
        if letter.isalnum():
            lettersStack.append(letter)

    for i in range(len(s)):
        if s[i].isalnum():
            if s[i].upper() != lettersStack.pop().upper():
                return False

    return True

def isPalindromeEff(s:str):
    if len(s) == 0:
        return True

    left, right = 0, len(s) - 1
    while left < right:
        while not s[left].isalnum() and left < len(s) - 1:
            left += 1

        while not s[right].isalnum() and right > 0:
            right -= 1

        if left > right:
            return True
        elif s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        else:
            return False

    return True


print(isPalindrome("A man, a plan, a canal: Panama"))