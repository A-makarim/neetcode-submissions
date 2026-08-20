class Solution:
    def checkValidString(self, s: str) -> bool:

        minopening = 0
        maxopening = 0

        for i in s:
            if i == "(":
                minopening +=1
                maxopening +=1
            if i == ")":
                minopening -=1
                maxopening -=1
            if i == "*":
                minopening -=1
                maxopening +=1
            if maxopening < 0: # meanings wwe have more closing brackets
                return False
            if minopening < 0: # we have more opening brackets
                minopening = 0 # reset to zero as we can chose not to use an opening bracket. more closing brackets alr reject at first
            
        return True if minopening == 0 else False



x = Solution()
assert x.checkValidString("(()*)") == True
        