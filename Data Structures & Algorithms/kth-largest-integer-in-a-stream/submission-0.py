class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums
        

    def add(self, val: int) -> int:
        self.stream.append(val)
        print(self.stream)
        sorted(self.stream)
        return self.stream[len(self.stream)-self.k]


        
