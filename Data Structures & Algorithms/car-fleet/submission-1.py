class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # we need the car with max max pos
        pair = [[p,s] for p,s in zip(position, speed)]
        pair.sort(key = lambda x: x[0], reverse = True)
        stack = []
        for i, j in pair:
            t = (target - i) / j
            stack.append(t)
            if len(stack) >=2:
                if stack[-1] <= stack[-2]:
                    stack.pop()
        return len(stack) 

        



        