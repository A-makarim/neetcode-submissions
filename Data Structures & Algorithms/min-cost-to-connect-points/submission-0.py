class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # use prims, start with any random index
        startingpoint = points[0]
        connected = set()
        totaldist = 0

        distances = [(0,0)]
        heapq.heapify(distances)
        while len(connected) < len(points):
            cost, idx = heapq.heappop(distances)
            i = points[idx]
            if idx in connected:
                continue
            connected.add(idx)
            for idx, j in enumerate(points):
                if idx not in connected:
                    dist = abs(i[0] -j[0]) + abs(i[1] - j[1])
                
                    heapq.heappush(distances, (dist, idx))
                # add all the distances
            # once all added. 
            # pop one and chec
            totaldist += cost
        return totaldist


        
        