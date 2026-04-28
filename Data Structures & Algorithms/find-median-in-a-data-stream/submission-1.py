class MedianFinder:

    def __init__(self):
        self.nums = []
        
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()
        print("added ", num)
        print("final", self.nums)
        

    def findMedian(self) -> float:
        ans = None
        leng = len(self.nums) # 2   # 3
        if leng % 2 == 1:    # zero    # 1
            print(self.nums)
            half = int(leng/2)     # 1.5  to 1
            print(half)
            ans = float(self.nums[half])   
            return ans

        else:
            print(leng)  # 2
            print(self.nums)
            middle = self.nums[int(leng/2)-1] + self.nums[int(leng/2)]   # 0 and 1 
            ans = float(middle/2)
            return ans

        
        