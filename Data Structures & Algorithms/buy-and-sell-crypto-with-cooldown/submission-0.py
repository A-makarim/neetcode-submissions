class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        length = len(prices)
        x = 0
        y = 0

        dp = {}

        def dfs(i, hold):
            nonlocal x, y

            if i >= length:
                return 0

            if (i, hold) in dp:
                return dp[(i, hold)]

            if not hold:
                skip = dfs(i+1, False)
                buy = (dfs(i+1, True) - prices[i])
                dp[(i, hold)] = max(skip, buy)
                return dp[(i, hold)]

            if hold:
                skip = dfs(i+1, True)
                keep = (dfs(i+2, False) + prices[i])
                dp[(i,hold)] = max(skip, keep)
                return dp[(i,hold)]

                
        return dfs(0, False)


             
        