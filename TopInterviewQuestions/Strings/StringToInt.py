"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.


Solution:

This question is really not hard. There are just a lot of edge cases.
There are faster solutions, but leverages regex.
"""


class Solution:
    def myAtoi(self, str) -> int:
        stripS = str.strip()
        isNegative = 1

        if stripS == "" or stripS == "-" or stripS == "+":
            return 0

        startIndex = 0
        if stripS[0] == "-":
            isNegative = -1
            startIndex += 1
        elif stripS[0] == "+":
            startIndex += 1

        if not stripS[startIndex].isdigit():
            return 0

        numArray = []

        while startIndex < len(stripS) and stripS[startIndex].isdigit():
            numArray.append(stripS[startIndex])
            startIndex += 1

        output = 0
        for i in range(len(numArray)):
            output += int(numArray[i]) * (10 ** (len(numArray) - i - 1))

        if output >= 2147483648 or output <= -2147483648:
            return 2147483647 if isNegative == 1 else -2147483648

        return isNegative * output


if __name__ == "__main__":
    solution = Solution()
    str = "42"
    print(solution.myAtoi(str))
