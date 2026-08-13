from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # we need a hashmap. i love hashmaps
        valandkey = defaultdict()
        

        
        for j, z in enumerate(nums):
            print(j, z)

            if target - z in valandkey:
                return [valandkey[target-z] ,j]

            valandkey[z] = j
assert Solution().twoSum([5, 5], 10) == [0,1]

print("success")
