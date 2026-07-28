class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        lenword1 = len(word1)
        lenword2 = len(word2)

        dp = {}
        

        def dfs(i , j):

            if (i, j) in dp:
                return dp[(i, j)]
            if i == lenword1:
                dp[(i, j)] = lenword2 -j
                return dp[(i, j)]

            if j == lenword2:
                dp[(i, j)] = lenword1 - i
                return dp[(i, j)]

            if word1[i] == word2[j]:
                dp[(i+1, j+1)] = dfs(i+1, j+1)
                return dp[(i+1, j+1)]

            dp[(i+ 1, j)] =  dfs(i + 1, j)
            dp[(i+ 1, j+1)] = dfs(i + 1, j + 1)
            dp[(i, j +1)] = dfs(i , j + 1)

            return 1 + min(
                
                dp[(i+ 1, j)], 
                dp[(i+ 1, j+1)],
                dp[(i, j +1)]

                
            )
        return dfs(0,0)
