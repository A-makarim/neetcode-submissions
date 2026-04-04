class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) -1
        mid = (left + right) //2

        while left <= right: 
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                # if you are bigger than left, means you are in left sorted.
                if target < nums[mid] and target >= nums[left]:
                    right = mid-1   # perfect, cut half right
                    mid = (left+right) //2
                else: # dw baby, 
                    left = mid + 1  
                    mid = (left+right) // 2
            else:
                # you are in right sorted. do you wanna search in right sorted? 
                if target > nums[mid] and target <= nums[right]: #keep searchning right
                    left = mid + 1  
                    mid = (left+right) // 2
                else: # no? oh baby. dw. move to left part
                    right = mid -1
                    mid = (left+right) // 2
        return -1
              # or you are in right sorted

        