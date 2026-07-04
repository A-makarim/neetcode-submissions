class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # go thru all the o(s)
        # check surrounding, 
        row = len(board)
        col = len(board[0])
        visited= set()
        change = []
        to_change = []
        free = False


        def dfs(r, c):
            nonlocal change, free
            if r < 0 or r == row or c < 0 or c == col or (r,c) in visited or board[r][c] == "X":
                return 
            if r == 0 or r == row -1 or c == 0 or c == col-1:
                free = True  
            visited.add((r, c))
            change.append([r, c])
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)

        
        for i in range(row):
            for j in range(col):
                free = False
                change = []
                if board[i][j] == "O":
                    dfs(i , j)
                if not free:
                    for r, c in change:
                        board[r][c] = "X"



            
        