class MedianFinder:

    def __init__(self):
        self.nums = []
        
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        

    def findMedian(self) -> float:
        leng = len(self.nums) # 2
        if leng % 2 == 1:    # zero
            half = int(leng/2)
            ans = float(self.nums[half])
            return ans

        else:
            print(leng)  # 2
            middle = self.nums[int(leng/2)-1] + self.nums[int(leng/2)]   # 0 and 1 
            ans = float(middle/2)
            return ans

        
        