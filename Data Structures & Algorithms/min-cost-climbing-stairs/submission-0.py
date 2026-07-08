class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        last = 0
        secondlast = 0

        for i in range(len(cost) -1 , -1, -1):

            print(i)

            temp = cost[i] + min(last, secondlast)
            secondlast = last
            last = temp

        return min(last, secondlast)            # take min 



        return 1