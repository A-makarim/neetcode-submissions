class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # permutation means:
        #   you have let's say 7 players
        #   what orders you can arrange them in 
        #   we just did combination
        #   but here order doesn't matter AT ALL (which is honestly great)

        # take a num, move on, don't take a num, move on

        res = []
        sublist = []

        def dfs(nums):
            if i==len(nums):
                res.append(list(sublist))
                return
 
            for i in nums:    # append each of the elemt firs once, and remove them   # NEW LIST WITH 
                sublist.append(i)   # add a num to list
                dfs(list(nums.remove(nums[i])))    # pass list without that num
                
        dfs(0)
        return res
            