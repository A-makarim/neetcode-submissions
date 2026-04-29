class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []  # we will return this, and addd results to this

        subset = [] # empty list, which will append to answer 
        def dfs(i): # takes in the iteration
            if i >= len(nums): # when no more numbers are left
                ans.append(list(subset))
                return
            subset.append(nums[i]) # include the ith num
            dfs(i+1)
            subset.pop() # remove from end
            dfs(i+1) # note that i here is same. hence a single dfs gives birth to two recursive dfs, with incremental i
        
        dfs(0) # start with oth index in nums
        return ans # retun the global ans


        