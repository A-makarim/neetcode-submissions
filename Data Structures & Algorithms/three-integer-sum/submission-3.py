class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        out = []
        print(nums)
        for i, n in enumerate(nums):
            print(n)
            left = i + 1
            right = l - 1
            if i == l-1:
                continue
            #if n == nums[i-1]: 
             #   continue 
            print ("left", left)
            print("right", right)
            while  left < right:
                print("running while")
                if n + nums[left] + nums[right] == 0:
                    out.append([n, nums[left], nums[right]])
                    left += 1
                    right -=1
                elif  n + nums[left] + nums[right] > 0:
                    right -= 1
                elif n + nums[left] + nums[right] < 0:
                    left += 1
        print(out, "===")
        out.sort()
        uni = []
        try:
            if len(out[0])>1:
                if isinstance(out[0], list):

                    for i,n in enumerate(out):
                        if i == len(out)-1:
                            uni.append(out[i])
                            continue
                        l = tuple(n)
                        
                        if l == tuple(out[i+1]):
                            continue
                        else:
                            uni.append(out[i])
        except:
            return out
        print(uni)
        return uni

        



