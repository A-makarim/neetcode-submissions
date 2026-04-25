class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # heappop will give lowest, we need highest, flip signs 

        stones = [-s for s in stones]

        # pop first
        heapq.heapify(stones)
        print(stones)
        first = heapq.heappop(stones)

        #keep destroying till last 

        while len(stones) >= 1:
            print(stones)
            second = heapq.heappop(stones)               # -2
            smash = first - second   # -7+3 is -4       -4 +2  is -2

            if smash != 0: 
                heapq.heappush(stones, smash)  # -4

            first = heapq.heappop(stones)              #-4
        return abs(first)



