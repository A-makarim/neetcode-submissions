class Solution:
    def rob(self, nums: List[int]) -> int:
        first = 0
        second = 0 

        for n in nums:
            temp = max(n + second, first)
            second = first
            first = temp

        return first

            

        