class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumarr = float('-inf')

        for i in range(len(nums)):
            sumarr = max(sumarr, sum(nums[:i+1]))
        for i in range(len(nums)):
            sumarr = max(sumarr, sum(nums[i:]))
        print(sumarr)
        return sumarr
            
        