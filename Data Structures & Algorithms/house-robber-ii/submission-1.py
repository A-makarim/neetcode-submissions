class Solution:
    def rob(self, nums: List[int]) -> int:

        

        def helper(nums):
            first = 0
            second = 0 
                # -2   -2    0
            # second, first, n 
            for n in nums:
                temp = max(n + second, first)
                second = first
                first = temp

            return first

        if len(nums) == 1:
            return nums[0]

        return max(helper(nums[1:]), helper(nums[:-1]))    

        