class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        lens1 = len(s1)
        lens2 = len(s2)
        lens3 = len(s3)
        def dfs(i , j):
            if i + j == lens3:
                return True

            if i < lens1:
                if s1[i] == s3[i+j]:
                    x = dfs(i+1,j)
                    if x:
                        return x
            if j < lens2:
                if s2[j] == s3[i+j]:
                    y = dfs(i, j+1)
                    if y:
                        return y
            return False
            
        if lens1 + lens2 != lens3:
            return False
        return dfs(0,0)

        