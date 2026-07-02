class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
                # return a 2d array
        row = len(grid)
        col = len(grid[0])
        visit = set()
        temp = deque()
        fresh = 0

        def bfs(r , c):
            nonlocal fresh
            if r >= row or r < 0 or c >= col or c < 0 or grid[r][c] in [0,2] or (r,c) in visit: 
                return
            temp.append([r, c])
            visit.add((r,c))
            grid[r][c] = 2
            fresh -=1


        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    temp.append([i, j])
                    visit.add((i, j))
                if grid[i][j] == 1:
                    fresh+=1
        time = 0
        while temp:
            for i in range(len(temp)):
                r , c = temp.popleft()
                bfs(r+1 ,c)
                bfs(r ,c+1)
                bfs(r ,c-1)
                bfs(r-1 ,c)
            if temp:
                time +=1 # very important. only add time if there is anything in temp after first loop. 
            print(len(temp))
        return -1 if fresh!= 0 else time
        