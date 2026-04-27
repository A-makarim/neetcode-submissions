from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # my first intuition is to do task with max reps. 
        # then do other tasks, once each. 
        # when all taks have been done once, 
        # see if n cycles have been done
        # and do tasks in same order. same empty cycles, same order, same empty cycles
        occurances = Counter(tasks)   # converts to dict
        heapq.heapify([occurances.values]) # this way we will have the most priority ot fetch
        print(occurances)

        leng = len(occurances)
        occurances = [[k, v] for k, v in occurances.items()]
        print(len(occurances))
        print(occurances[0][0])
        steps = 0
        new = []
        while occurances:

            new = []
            resett = 0

            for i in range(len(occurances)):
                resett +=1
                steps +=1

                occurances[i][1] -=1

                if occurances[i][1] > 0:
                    new.append(occurances[i])
            occurances = new
            while resett < n + 1 and occurances:
                steps +=1
                resett +=1

        return steps


        