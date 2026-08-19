class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        count = {}
        for i in hand:
            count[i] = 1 + count.get(i, 0)
        minheap = list(count.keys())
        heapq.heapify(minheap)
        while minheap:
            lowest = minheap[0]
            for i in range(lowest, lowest + groupSize):
                if i in count:
                    count[i] -=1
                else:
                    return False
                # we just rmeoved an entire group. now we find the next lowest and do the same
                if count[i] == 0:
                    if i == minheap[0]:
                        heapq.heappop(minheap)
                    else:
                        return False

        return True
