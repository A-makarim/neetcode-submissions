class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp  = [[None]*(n) for i in range(m)]   
        print(dp) 

        def dfs(i , j):
            if i > m-1 or j > n-1:  # n = 3, n-1 = 2. 2>2 no. 3 > 2 yes 
                return 0
            print(i, j)

            if dp[i][j]:
                return dp[i][j]

            if i == m-1 and j == n-1:
                return 1


            dp[i][j] = dfs(i+1, j) + dfs(i, j+1)
            
                

            

            return dp[i][j]
            

        dfs(0, 0)
        return dp[0][0]
        