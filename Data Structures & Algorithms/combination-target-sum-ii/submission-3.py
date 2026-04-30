"""
KEY INSIGHTS
NOTICE WHILE LOOP WHICH IS NEW HERE 
why? cuz imagine if we popping, and there are two instances, we include it again, so we get same number of that element in two diff subsets
"""



class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # each number can be used at most once, which means you can not include, or pop and move on
        # there was be duplicate numbers?

        # the idea is you can use a number appearing twice twice in a list. 
        # but you cant make same combination given two diff in
    
        res = []; 
        sublist = []

        candidates.sort()

        def dfs(i, total):

            if total == target:
                res.append(list(sublist))
                return
            
            if total > target:
                return
            
            if i == len(candidates):
                return

            sublist.append(candidates[i])
            total = total + candidates[i]
            dfs(i+1, total)  # we are alr including the additional duplicate

            sublist.pop() # we remvoed the additional duplicate and retry
            total = total - candidates[i]
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]: # why? cuz imagine if we popping, and there are two instances, we include it again, so we get same number of that element in two diff subsets
                i+=1
            
            dfs(i+1, total) # we might again just get additional duplicate
            

        dfs(0, 0); return res

            
        
        