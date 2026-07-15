class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lenght = len(nums)

        dp = [1] * lenght    #### CACHE

        def dfs(i):
            if dp[i] != 1:  #### MEMORIZATION CASE
                return dp[i]
            longest =1 

            for j in range(i+1 , lenght):
                if nums[i] < nums[j]:
                    longest = max(longest, 1 + dfs(j))  # dfs(j) is alr the longest. +1 determines if to include or not

            dp [i] = longest  #### CACHE STORE 
            return longest
        ans = 1

        for i in range(lenght):
            ans = max(ans, dfs(i))
        return ans

        