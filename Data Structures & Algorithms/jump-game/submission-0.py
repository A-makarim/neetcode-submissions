class Solution:
    def canJump(self, nums: List[int]) -> bool:

        leng = len(nums) # 5
        i = 0

        while i < leng -1:   #3 < 5-1   4 no, so doesn't run
            if nums[i] == 0:
                return False
            i = i + nums[i]

        if i == leng -1:
            return True
        else:
            return False  
        