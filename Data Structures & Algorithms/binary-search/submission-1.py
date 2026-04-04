class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # array is alr sorted

        left = 0
        right = len(nums) -1 

        # left is min
        # right is max
        if target < nums[0]:
            return -1

        # mid must be calculated. 
        while left <= right:
            
            mid = (left + right)//2
            # interget mid is calc
            print("mid", mid)  # to debug
            if nums[mid] == target:
                return mid  

            if left == right:
                return -1 
            else: 
                # teo cases exist. move irght or left
                if nums[mid] > target:
                    # search left array 
                    right = mid -1
                else: 
                    # mid nums is lesser. hence move right
                    left = mid +1


