class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        theset = set(nums)
        if len(theset) == len(nums):
            return False
        else:
            return True
        