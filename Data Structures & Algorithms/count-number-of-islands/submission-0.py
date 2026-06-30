class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        path = set() # we will store all the locations we have reached
        row = len(grid)
        col = len(grid[0])


        def dfs(r,c):
            if  r >= row or r < 0 or c >= col or c < 0 or (r,c) in path or grid[r][c] == "0":
                return False
            path.add((r ,c))
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)
            return True


        for i in range(row):
            for j in range(col):
                if dfs(i,j):
                    res +=1
        return res
        



        
        