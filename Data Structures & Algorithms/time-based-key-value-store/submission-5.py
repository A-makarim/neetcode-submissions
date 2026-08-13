class TimeMap:

    def __init__(self):
        self.h = defaultdict(list)

    # list is alr sorted

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.h[key].append([value, timestamp])
        return

    def get(self, key: str, timestamp: int) -> str:
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
        
