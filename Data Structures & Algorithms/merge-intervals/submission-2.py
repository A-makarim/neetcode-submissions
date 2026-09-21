class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len(intervals)
        res = []
        i = 1
        first = intervals[0]
        while i < n:
            # we will merge two at a time
            second = intervals[i]
            if first[1] < second[0]:
                res.append(first)
                i+=1
                first = second
                print(first)
                
            else:
                newstart = min(first[0], second[0])
                newend = max(first[1], second[1])
                # res.append([newstart, newend])
                i+=1
                first = [newstart, newend]
        res.append(first)

        return res