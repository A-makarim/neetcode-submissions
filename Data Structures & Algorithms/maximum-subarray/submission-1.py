class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumarr = float('-inf')

        for i in range(len(nums)):
            for j in range(len(nums)):
                sumarr = max(sumarr, sum(nums[i:j+1]))
        return sumarr
            
        