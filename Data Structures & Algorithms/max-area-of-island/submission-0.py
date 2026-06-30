class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        path = set() # we will store all the locations we have reached
        row = len(grid)
        col = len(grid[0])
        big = 0
        high = 0


        def dfs(r,c):
            nonlocal big
            if  r >= row or r < 0 or c >= col or c < 0 or (r,c) in path or grid[r][c] == 0:
                return False
            big = big +1
            path.add((r ,c))
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)
            return True


        for i in range(row):
            for j in range(col):
                if dfs(i,j):
                    high = max(big, high)
                    big =0

        return high
        