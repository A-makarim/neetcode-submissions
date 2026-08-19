class Solution:
    def canJump(self, nums: List[int]) -> bool:

        leng = len(nums) # 5
        # for num in every index, we want the max in that slice

        def dfs(i):
            if i >= leng-1:
                return True
            if nums[i] == 0:
                return False
            for j in range(1, nums[i]+1):
                if dfs(i+j):
                    return True
            return False

        return dfs(0)