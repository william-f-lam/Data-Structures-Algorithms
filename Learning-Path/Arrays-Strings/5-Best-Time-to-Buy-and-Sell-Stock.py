# Leetcode #121

# Prompt: You are given an array prices where prices[i] is the price of a given stock on the ith day.
#         You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#         Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Solution:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Start out by testing a buy on day 1.
        buyPrice = prices[0]
        # To avoid negative profit, set the initial max profit to 0.
        maxProfit = 0
        
        for price in prices:
            # Profit from the current sell price, minus the minimum buy price found before.
            currentProfit = price - buyPrice
            # Keep only the largest profit.
            maxProfit = max(maxProfit, currentProfit)
            # Find and store only the smallest buy price and move forward.
            buyPrice = min(buyPrice, price)
        return maxProfit

        # Time Complexity: O(n)
        # Space Complexity: O(1)
