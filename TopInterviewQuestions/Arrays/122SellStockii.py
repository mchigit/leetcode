"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.



Idea:

Loop through the array, as long as current number is greater than previous number, add the difference to total

"""

from typing import List


def maxProfit(prices: List[int]) -> int:
    if len(prices) == 1:
        return 0

    total = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            total += (prices[i] - prices[i - 1])

    return total


if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    profit = maxProfit(nums)
    print(profit)