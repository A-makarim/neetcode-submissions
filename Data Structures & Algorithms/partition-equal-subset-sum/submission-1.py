class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        length = len(nums)
        if total%2 != 0:
            return False

        def dfs(i , carry):
            if i >= length:
                return False
            if carry + nums[i] == total/2:
                return True
            if carry + nums[i] > total/2:
                return False

            x = dfs(i+1, carry)
            if x:
                return x
            y = dfs(i+1, carry + nums[i])
            if y:
                return y
            
        return dfs(0 , 0) if dfs(0, 0) else False
