class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        minheap = []
        lencol = len(grid[0])
        lenrow = len(grid)
        minheap.append((grid[0][0], 0, 0))   # max row col
        heapq.heapify(minheap)
        visited = set()
        while minheap:
            maxx, i, j = heapq.heappop(minheap)
            if (i,j) in visited:
                continue
            visited.add((i,j))
            if i == lenrow -1 and j == lencol-1:
                return maxx

            if i + 1 >= 0 and i + 1 < lenrow-1 and (i+1,j) not in visited:
                heapq.heappush(minheap, (max(grid[i+1][j], maxx), i+1, j))
            if i - 1 >= 0 and i - 1 < lenrow-1 and (i-1,j) not in visited:
                heapq.heappush(minheap, (max(grid[i-1][j], maxx), i-1, j))
            if j + 1 >= 0 and j + 1 < lencol-1 and (i,j+1) not in visited:
                heapq.heappush(minheap, (max(grid[i][j+1], maxx), i, j+1))
            if j - 1 >= 0 and j - 1 < lencol-1 and (i,j-1) not in visited:
                heapq.heappush(minheap, (max(grid[i][j-1], maxx), i, j-1))
            