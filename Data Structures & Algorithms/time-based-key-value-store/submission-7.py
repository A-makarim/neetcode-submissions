from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.h = defaultdict(list)

    # list is alr sorted

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.h[key].append([value, timestamp])
        return

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.h.get(key, [])
        x = len(self.h[key]) 
        l, r = 0 , x -1
        while l <= r:
            m = (l+r) // 2
            if values[m][1] <= timestamp:
                res = self.h[key][m][0]
                l = m +1
            else:
                r = m-1
        
        return res


        for i in self.h[key]: 
            if i[1] == timestamp:  # iterating over values 10 not equal to 1
                return i[0]

        # first loops gives the valeu at that timestmap. now you might now find that timestamp.
        # find largest before it 
        maxx = 0 
        for i in self.h[key]:
            if i[1] < timestamp:
                maxx = max( maxx, i[1]) # max is 10 we keep max 10
                

        for i in self.h[key]:   # 
            
            if i[1] == maxx:   # not max
                return i[0]
        return ""
        
