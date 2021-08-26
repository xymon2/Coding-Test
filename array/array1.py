#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
# 시간복잡도 신경쓰는게 어렵다.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10000
        result = 0

        for stock in prices:
            min_price = min(stock, min_price)
            result = max(stock - min_price, result)

        return result