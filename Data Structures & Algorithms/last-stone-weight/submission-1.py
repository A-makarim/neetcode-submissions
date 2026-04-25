class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # heappop will give lowest, we need highest, flip signs 

        stones = [-s for s in stones]

        # pop first
        first = heapq.heappop(stones)

        #keep destroying till last 

        while len(stones) >= 1:
            second = heapq.heappop(stones)
            smash = abs(first - second)

            heapq.heappush(stones, smash)

            first = heapq.heappop(stones)
        return abs(first)



