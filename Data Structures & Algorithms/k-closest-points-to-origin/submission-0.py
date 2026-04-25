class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # simple brute force is 
        #   find dist for all points
        #   return k closest. 

        # can you somehow know this before calculating dist?
        # before the actual fomrula? 

        # or rather lets say you compute for all of them
        # now return the k clothes. 
        # you can do heapq k times. or sort and return. this is the only plce i cna thing of decreasing complexity
        # thinking...
        # also one more thing. you cal abs() value. you get an ans. but you need to return actual point. not abs() 
        # can do a mapping. dict? 

        def finddist(l):
            ans =  ((l[0])**2 + (l[1])**2)
            return ans

        #compute dist for all
        new_list = []
        final = []
        for i in points:
            andd = finddist(i)
            new_list.append([andd, i])

        heapq.heapify(new_list)
        
        for i in range(k):
            a = heapq.heappop(new_list)
            final.append(a[1])


        

        return final