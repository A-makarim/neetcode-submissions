class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        lenght = len(coins)

        dp = [[None]*(amount+1) for i in range(lenght+1)]


        def dfs(i, remaining):
        
            if remaining < 0 or i >= lenght:
                return 0
            if dp[i][remaining] is not None:
                return dp[i][remaining]
            if remaining == 0: 
                dp[i][remaining] = 1
                return 1

            
            dp[i][remaining] =  dfs(i, remaining-coins[i]) + dfs(i+1, remaining)
            return dp[i][remaining]
    
        return dfs(0, amount)
