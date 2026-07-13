class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s)+1)   # for a 3 letter word, 0 ,1 , 2, 3

        # the last segment cna be true
        dp[len(s)] = True    # should be able to segment as 3. it's an empty string

        for i in range(len(s)-1, -1, -1):  # goes till zero, with -1 step
            for w in wordDict: # take one word:
                x = len(w)    # let's check if this word in last suffix
                if (i + x < len(s)) and s[i: i +x] == w:
                    dp[i] = True
                if dp[i]:
                    break
        return dp[0]
        