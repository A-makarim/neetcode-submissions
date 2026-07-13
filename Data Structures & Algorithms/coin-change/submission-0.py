class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def dfs(amount):
            if amount == 0:
                return 0

            ans = float("inf")

            for coin in coins:
                if amount >= coin:
                    ans = min(ans, 1 + dfs(amount - coin))

            return ans
        x = dfs(amount)
        if x == float('inf'):
            return -1
        return x


        

