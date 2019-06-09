"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

Solution:

Notice a patter. The row number increases from 0 to numRows - 1, then starts decreasing.
So we just loop through the string, append it to the correct row, we can ignore the spaces since we don't print it
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows > len(s) or numRows == 1:
            return s

        output = ["" for x in range(numRows)]
        row, step = 0, 1

        for c in s:
            output[row] += c
            if row == 0:
                step = 1
            elif row == (numRows - 1):
                step = -1
            row += step

        outputString = ""
        for rowString in output:
            outputString += rowString

        return outputString
