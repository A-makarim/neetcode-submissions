class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # return a 2d array
        row = len(grid)
        col = len(grid[0])
        visit = set()
        q = deque()

        def bfs(r , c):
            if r >= row or r < 0 or c >= col or c < 0 or grid[r][c] == -1 or (r,c) in visit: 
                return
            temp.append((r, c))
            visit.add(r,c)


            for i in range(row):
                for j in range(col):
                    if grid[i][j] == 0:
                        q.append([i, j])
                        visit.add(i, j)
            dist = 0
            while q:
                for i in range(len(q)):
                    r , c = q.popleft()
                    room[r][c] = dist
                    bfs(r+1 ,c)
                    bfs(r ,c+1)
                    bfs(r ,c-1)
                    bfs(r-1 ,c)
                dist +=1 


             
        