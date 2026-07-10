class Solution:
    def longestPalindrome(self, s: str) -> str:

        def ispalindrome(arr):
            x = len(arr)

            if x%2 != 0:
                mid = int(x/2) + 1
                l = mid-1
                r = mid-1
                print(mid)
            else:
                mid = int(x/2)
                l = mid-1
                r = mid

            while l >= 0 and r < x :

                if arr[l] == arr[r]:
                    l -=1
                    r +=1
                else:
                    return arr[l+1:r]
            return arr[l+1:r]
        ans = []
        x = len(s)
        for i in range(x):
            ans.append(ispalindrome(s[:i+1]))
        return max(ans)



        