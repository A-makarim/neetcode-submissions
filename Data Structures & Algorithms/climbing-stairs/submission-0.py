class Solution:
    def climbStairs(self, n: int) -> int:

        last = 1
        secondlast = 1

        for i in range(n-1):
            temp = secondlast
            secondlast = secondlast + last
            last = temp

        return secondlast        