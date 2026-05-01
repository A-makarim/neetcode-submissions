class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # permutation means:
        #   you have let's say 7 players
        #   what orders you can arrange them in 
        #   we just did combination
        #   but here order doesn't matter AT ALL (which is honestly great)

        # take a num, move on, don't take a num, move on

        if len(nums) == 0:
            return [[]]

        sublists = self.permute(nums[1:])   # re call permute but remove first element
        res = []

        for alist in sublists:
            for i in range(len(alist)+1 ):
                alist_copy = alist.copy()
                alist_copy.insert(i , nums[0])
                res.append(alist_copy)

        return res






        dfs(0)
        return res
            