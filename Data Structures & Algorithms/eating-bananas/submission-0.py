class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        l = 1
        r = max(piles)
        answer = r

        while l <= r:
            speed = (l + r) // 2
            hours = 0

            for pile in piles:
                hours += (pile + speed - 1) // speed  # ceiling division

            if hours <= h:
                answer = speed
                r = speed - 1       # try a slower speed
            else:
                l = speed + 1       # speed is too slow

        return answer


        