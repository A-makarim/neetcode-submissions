from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.h = defaultdict(list)

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.h[key].append([value, timestamp])
        return

    def get(self, key: str, timestamp: int) -> str:
        for i in self.h[key]:
            if i[1] == timestamp:  # iterating over values
                return i[0]
        leng = len(self.h[key])
        for i in self.h[key]:
            if i[1] == leng:
                return i[0]        
        
