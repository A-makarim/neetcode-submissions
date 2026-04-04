class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        for i,n in enumerate(prices):
            m = max( max(prices[i:]) - n , m   )

        return m
        