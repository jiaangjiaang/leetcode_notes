class Solution:
    def maxProfit(prices):
        minprice = prices[0]
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit



prices = [7, 1, 5, 3, 6, 4]
prices_1 = [1, 2]

print(Solution.maxProfit(prices_1))