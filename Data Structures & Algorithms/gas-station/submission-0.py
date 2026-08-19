class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        start = 0 

        if sum(gas) - sum(cost) < 0:
            return -1 

        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                start = i+1
                print(start)
                total = 0
        return start