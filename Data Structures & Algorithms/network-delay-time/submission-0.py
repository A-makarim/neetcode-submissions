class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)

        for x,y,z in times:
            adj[x].append((z , y))
        # we have a node, its neighbour and time in a tuple
        minheap = []
        minheap.append((0, k)) # we don't need any time for k 
    
        visit = set()
        res = 0 

        while minheap:
            time , node = heapq.heappop(minheap)
            if node in visit:
                continue

            visit.add(node)
            res = max(time, res)

            for timenb, neighbours in adj[node]:
                if neighbours in visit:
                    continue
                heapq.heappush(minheap, ( timenb + time , neighbours))
        
        return res if len(visit) == n else -1

         



        