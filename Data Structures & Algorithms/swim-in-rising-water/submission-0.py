class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        minheap = []
        lencol = len(grid[0])
        lenrow = len(grid)
        minheap.append((grid[0][0], 0, 0))   # max row col
        heapq.heapify(minheap)
        visited = set()
        visited.add((0,0))
        while minheap:
            maxx, i, j = heapq.heappop(minheap)
            visited.add((i,j))
            if i == lenrow -1 and j == lencol-1:
                return maxx
            if i >= 0 and i < lenrow-1 and (i+1,j) not in visited:
                heapq.heappush(minheap, (max(grid[i+1][j], maxx), i+1, j))
            if i >= 0 and i < lenrow-1 and (i-1,j) not in visited:
                heapq.heappush(minheap, (max(grid[i-1][j], maxx), i-1, j))
            if j >= 0 and j < lencol-1 and (i,j+1) not in visited:
                heapq.heappush(minheap, (max(grid[i][j+1], maxx), i, j+1))
            if j >= 0 and j < lencol-1 and (i,j-1) not in visited:
                heapq.heappush(minheap, (max(grid[i][j-1], maxx), i, j-1))
            