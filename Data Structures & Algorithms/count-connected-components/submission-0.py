class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # no repeated edges, not circular.
        ans = n - len(edges)
        return ans
        if n-1 == len(edges):
            return 1  # everything is connected to each other and no circular edges. so 1 single component

        # keep track of visited. then start with min of not visited. 

        visited = set() # lookup of 0(1)

            
         
        