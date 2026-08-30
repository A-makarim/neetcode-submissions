class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        lencol = len(matrix[0])
        lenrow = len(matrix)
        dp = {}
        def dfs(r,c, prevval):
            if r < 0 or c < 0 or r >= lenrow or c >= lencol or matrix[r][c] <= prevval: # cuz strictly inc
                return 0 # cuz we will keep adding len
            if (r,c) in dp:
                return dp[(r,c)]
            addinglen = 1 # if it's strictly increasing

            # now we wanna try 4 directions
            addinglen = max(addinglen, 1 + dfs(r +1 , c, matrix[r][c]))
            addinglen = max(addinglen, 1 + dfs(r -1 , c, matrix[r][c]))
            addinglen = max(addinglen, 1 + dfs(r  , c-1, matrix[r][c]))
            addinglen = max(addinglen, 1 + dfs(r  , c+1, matrix[r][c]))

            dp[(r,c)] = addinglen
            return dp[(r,c)]
        ans = 0
        for i in range(lenrow):
            for j in range(lencol):
                ans = max(ans, dfs(i, j, -1))


        return ans
