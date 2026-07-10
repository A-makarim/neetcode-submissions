class Solution:
    def longestPalindrome(self, s: str) -> str:

        def ispalindrome(arr):
            x = len(arr) -1

            if x%2 != 0:
                mid = int(x/2) + 1
                l = mid
                r = mid
            else:
                mid = x/2
                l = int(mid)
                r = int(mid+1)

            while l >= 0 and r < x + 1:

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



        