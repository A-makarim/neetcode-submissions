class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        lens1 = len(s1)
        lens2 = len(s2)
        lens3 = len(s3)
        dp = {}
        def dfs(i , j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i + j == lens3:
                dp[(i, j)] = True
                return dp[(i, j)]

            if i < lens1:
                if s1[i] == s3[i+j]:
                    dp[(i, j)] = dfs(i+1,j)
                    if dp[(i, j)]:
                        return dp[(i, j)]
            if j < lens2:
                if s2[j] == s3[i+j]:
                    dp[(i, j)] = dfs(i, j+1)
                    if dp[(i, j)]:
                        return dp[(i, j)]
            return False
            
        if lens1 + lens2 != lens3:
            return False
        return dfs(0,0)

        