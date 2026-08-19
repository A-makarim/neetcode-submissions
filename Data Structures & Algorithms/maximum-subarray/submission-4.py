class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestsum = float('-inf')
        currsum = nums[0]

        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums)):
            if currsum + nums[i] > nums[i]:
                currsum += nums[i]
                bestsum = max(bestsum, currsum)
                
            else:
                currsum = nums[i]
                bestsum = max(bestsum, currsum)
            
        return bestsum 
        