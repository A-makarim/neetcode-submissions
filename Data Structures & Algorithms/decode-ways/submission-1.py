class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):  # index of the digit 
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i+1)   # will follow the hashhing.

            if (i+1 < len(s) and (s[i] == "1" or s[i]== "2" and s[i+1] in "0123456")):
                res += dfs(i+2) #so dp 1 means th number of ways to decode 1 onwards



            dp[i] = res  # updating the has here. first hash is alr there
            return res

        return dfs(0)
            
            
