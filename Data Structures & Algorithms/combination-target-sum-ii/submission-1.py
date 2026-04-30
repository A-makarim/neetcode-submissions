class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # each number can be used at most once, which means you can not include, or pop and move on
        # there was be duplicate numbers?
    
        res = []; sublist = []

        candidates.sort()

        def dfs(i):

            if sum(sublist) == target:
                if sublist not in res:
                    res.append(list(sublist))
                return
            
            if sum(sublist) > target:
                return
            
            if i >= len(candidates):
                return

            sublist.append(candidates[i])
            dfs(i+1)

            sublist.pop()
            dfs(i+1)

        dfs(0); return res

            
        
        