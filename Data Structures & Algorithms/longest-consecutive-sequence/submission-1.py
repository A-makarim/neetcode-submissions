class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lon = 1
        n = set(nums)
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if nums[i] - 1 in n:
                # yes there is lesser, don't make start of seq
                continue
            else:
                # doesnt? this is our start, check its consecutive!
                seq = 1
                # now following thru the chain
                while nums[i] + seq in n:
                    seq +=1 
                else:
                    lon = max(lon, seq)



        return lon
        