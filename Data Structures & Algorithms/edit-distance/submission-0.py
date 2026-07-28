class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        lenword1 = len(word1)
        lenword2 = len(word2)
        

        def dfs(i , j):
            if i == lenword1:
                return lenword2 - j

            if j == lenword2:
                return lenword1 - i

            if word1[i] == word2[j]:
                    return dfs(i+1, j+1)

            return 1 + min(
                dfs(i + 1, j),  # skipping or delete
                dfs(i + 1, j + 1), # replacing
                dfs(i , j + 1) # inserting
                
            )
        return dfs(0,0)
