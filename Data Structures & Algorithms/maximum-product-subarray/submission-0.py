class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmax = 1
        currmin = 1

        res = max(nums)  # this is the minimum threshold 

        for i in nums:   # we iterate thru this
            temp = currmax
            currmax = max(i, i*currmax, i*currmin)  #2 
            print(currmax)
            currmin = min(i, i*temp,    i*currmin)  #1 

            res = max(res, currmax) 
        return res
        