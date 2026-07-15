class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lenght = len(nums)

        dp = [None] * lenght    #### CACHE

        def dfs(i):
            if dp[i] != None:  #### MEMORIZATION CASE
                return dp[i]
            dp[i] =1 

            for j in range(i+1 , lenght):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i] , 1 + dfs(j))  # dfs(j) is alr the longest. +1 determines if to include or not

            #dp [i] = longest  #### CACHE STORE 
            return dp[i]
        for i in range(lenght):
            dfs(i)

        return max(dp)

        