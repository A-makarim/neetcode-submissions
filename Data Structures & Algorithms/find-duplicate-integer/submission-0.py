class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # nums = [1,2,3,2,2]
        # 2

        slow = 0
        fast = 0

        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow!= fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # as per floyds alg, another slow and prev slow should meet at same place.

        slow2 = 0

        while slow2!= slow:
            slow = nums[slow]
            slow2 = nums[slow2]

        # the number is a duplicate:
        print(slow2)

        return slow
            
        

        






        

        
        