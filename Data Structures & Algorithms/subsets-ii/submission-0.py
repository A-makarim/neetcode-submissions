class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # this is diff from subset as it can contain duplicates. 

        res = []
        sublist = []
        nums.sort()

        def dfs(i):
            if i == len(nums):
                res.append(list(sublist))
                return

            sublist.append(nums[i])
            dfs(i+1)

            sublist.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i +=1
            dfs(i+1)  # here is the thing. if you i is a duplicate element, you 
        
        dfs(0)
        return res