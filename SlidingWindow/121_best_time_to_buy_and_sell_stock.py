from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return max_profit


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        l, r = 0, 1
        max_profit = 0
        while r < n:
            while l < n - 1 and prices[l+1] <= prices[l]:
                l += 1
            while r < n - 1 and prices[r+1] >= prices[r]:
                r += 1

            profit = prices[r] - prices[l]
            max_profit = max(profit, max_profit)
            r += 1
            if prices[r] < prices[l]:
                l = r
                r = r + 1
        return max_profit


# Test
prices = [4, 3, 5, 7, 2]
res = Solution().maxProfit(prices)
print(res)
assert res == 4


"""
121. Best Time to Buy and Sell Stock
Easy
Topics
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
