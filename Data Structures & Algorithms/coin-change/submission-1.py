class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # for every state, we need the min coins

        dp = [float("inf")] * (amount + 1)

        dp [0] = 0

        print(dp)

        def dfs(amount):
            if amount < 0: # you can not use this path, return inf, 
                return float('inf')

            if dp[amount] != float('inf'): # you can use pre computed values
                return dp[amount]

            ans = dp[amount] # this can be infinity
            for i in coins: # iterate on every coin
                ans = min( 1 + dfs(amount - i), ans)
            
            dp[amount] = ans
            return ans


        dfs(amount)
        return dp[amount] if dp[amount] != float('inf') else -1


        

