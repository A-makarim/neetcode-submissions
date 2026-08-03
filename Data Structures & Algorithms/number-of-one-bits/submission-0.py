class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        # while(n):
        #     count += n &1
        #     n >>= 1

        # return count
        
        while(n):
            n = n & (n-1)   # removes the last 1. trailing zeroes
            count +=1

        return count