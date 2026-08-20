class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # use prims, start with any random index
        connected = set()
        totaldist = 0
        distances = [(0,0)]
        heapq.heapify(distances)

        while len(connected) < len(points):
            cost, idx = heapq.heappop(distances)
            if idx in connected:
                continue
            connected.add(idx)

            totaldist += cost

            i = points[idx]

            for idx, j in enumerate(points):
                dist = abs(i[0] -j[0]) + abs(i[1] - j[1])
                heapq.heappush(distances, (dist, idx))

        return totaldist


        
        