class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rowlen = len(heights)
        collen = len(heights[0])
        def dfs(r, c, visited, prev):
            # we are sure that this will be in visited

            if r < 0 or c < 0 or r >= rowlen or c>= collen or (r,c) in visited:
                return

            if prev > heights[r][c]:
                return

            #if prev <= heights[r][c]:
            visited.add((r, c))

            
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            
            return
        pac = set()
        atl = set()
        # first row and col
        for i in range(rowlen):
            dfs(i, 0, pac, -1)
        for j in range(collen):
            dfs(0, j, pac, -1)
        for i in range(rowlen):
            dfs(i, collen-1, atl, -1)
        for j in range(collen):
            dfs(rowlen-1, j, atl, -1)

        return list(pac & atl)