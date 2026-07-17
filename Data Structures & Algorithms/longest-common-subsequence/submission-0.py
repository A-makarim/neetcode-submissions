class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        leni = len(text1)
        lenj = len(text2)

        def dfs(i, j):
            if i >= leni or j >= lenj:   
                return 0

            if text1[i] == text2[j]:
                return 1 + dfs(i+1, j+1)
            
            return max(dfs(i+1, j) , dfs(i, j+1))
            
        return dfs(0,0)

             

        