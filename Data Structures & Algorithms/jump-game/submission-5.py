class Solution:
    def canJump(self, nums: List[int]) -> bool:

        leng = len(nums) - 1 # as we need index

        for i in range(len(nums) -1 , -1, -1):
            if nums[i] + i >= leng:
                leng = i

        return True if leng == 0 else False

        