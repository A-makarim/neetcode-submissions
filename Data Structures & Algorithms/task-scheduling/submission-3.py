from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # my first intuition is to do task with max reps. 
        # then do other tasks, once each. 
        # when all taks have been done once, 
        # see if n cycles have been done
        # and do tasks in same order. same empty cycles, same order, same empty cycles
        occurances = Counter(tasks)   # converts to dict
        occurances = [-s for s in occurances.values()]
        print(occurances)
        heapq.heapify(occurances) # this way we will have the most priority ot fetch
        print(occurances)
        steps = 0


        while occurances: 
            required = 0
            temp = []

            for i in range(n+1):
                if occurances: 
                    removed = heapq.heappop(occurances)
                    print(removed)
                    removed +=1
                    steps +=1
                    required +=1

                    if removed < 0 :
                        temp.append(removed)

                else:
                    if not temp: return steps
                    required +=1
                    steps +=1


                # temp should go back in once required is < n + 1
               

            for i in temp:
                heapq.heappush(occurances, i)

            if not occurances:
                return steps



        return steps