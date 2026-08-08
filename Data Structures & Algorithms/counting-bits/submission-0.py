class Solution:
    def countBits(self, n: int) -> List[int]:

        dp = [0] * (n+1)
        powerneeded = 1
        for i in range(1, n+1):
            if powerneeded*2 == i:
                powerneeded = i

            dp[i] = dp[i - powerneeded] + 1
 
        return dp
obj = Solution()

print(Solution.countBits(obj, 16))


        
