class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')]*n
        dist[src] = 0
        print(dist)

        for i in range(k+1):
            temp = dist.copy()
            for fr, to, price in flights:
                if dist[fr] != float('inf') and dist[fr] + price < temp[to]:
                    temp[to] = dist[fr] + price

            dist = temp
                
        return -1 if dist[dst] == float('inf') else dist[dst]
        
        