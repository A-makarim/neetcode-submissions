from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        pre = 1
        for i, n in enumerate(nums):
            prod = n * pre
            pre = prod
            out.append(prod)
        post = 1
        print(out)
        l = len(nums)
        for i , n in enumerate(out):
            c = l-i-1
            print(c)
            if c == 0:
                print(post, nums[c-1])
                out[c] = post 

            else:
                print(post, nums[c-1])

                out[c] = post * out[c-1]
            post = post * nums[c]
            


       # for i, n in enumerate(nums):
        return out
            


