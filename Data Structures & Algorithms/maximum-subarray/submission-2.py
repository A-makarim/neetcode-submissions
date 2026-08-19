class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestsum = float('-inf')
        currsum = float('-inf')
        
        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            if currsum + nums[i] > nums[i]:
                bestsum = currsum + nums[i]
                currsum += nums[i]
            else:
                bestsum = currsum
                currsum = nums[i]

        return bestsum 
        