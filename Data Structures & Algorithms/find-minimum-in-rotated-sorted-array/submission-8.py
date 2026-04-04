class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1
        mid = (left + right)//2
        m = 100000
        while left <= right:
            if nums[left] < nums[right]:
                return min(m, nums[left])
            mid = (left+right)//2  
            print(mid)
            print(nums[mid])
            m = min(nums[mid], m)
            print(m)
            if nums[mid] < nums[left]:
                # you are in right sorted portion, search left
                right = mid -1
            else:
                # you are in left sorted portion, search right
                left = mid+1

        return m