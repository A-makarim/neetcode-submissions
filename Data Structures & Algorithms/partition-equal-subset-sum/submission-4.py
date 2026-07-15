class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        

        total = sum(nums)
        length = len(nums)
        if total%2 != 0:
            return False
        else:
            target = total//2

        dp = [[None] *(target+1) for i in range(length)]

        def dfs(i , carry):
            if carry  == total/2:
                return True
            if i >= length:
                return False

            if carry  > total/2:
                return False

            if dp[i][carry] != None:
                return dp[i][carry]
            else:
                x = dfs(i+1, carry)
                y = dfs(i+1, carry + nums[i])
                if x:
                    dp[i][carry] = x
                    return True
                elif y:
                    dp[i][carry] = y
                    return True
            dp[i][carry] = False

            return False
            
        return dfs(0 , 0)
