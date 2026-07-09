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

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))    

        