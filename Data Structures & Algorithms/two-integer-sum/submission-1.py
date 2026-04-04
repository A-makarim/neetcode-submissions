class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ph= {}
        for i , n in enumerate(nums):
            diff = target - n
            if diff in ph:
                return [ph[diff], i]
            ph[n] = i 