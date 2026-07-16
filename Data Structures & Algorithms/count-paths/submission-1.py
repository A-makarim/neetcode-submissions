class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = 0

        def dfs(i , j):
            nonlocal paths
            if i == m-1 and j == n-1:
                return 1
            if i > m-1 or j > n-1:
                return 0

            row = dfs(i+1, j)
            if row==1:
                paths += 1
                

            col = dfs(i, j+1)
            if col==1: 
                paths += 1

            

        dfs(0, 0)
        return paths

        