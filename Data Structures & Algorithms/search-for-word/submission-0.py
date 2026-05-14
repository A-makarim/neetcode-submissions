class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        res = False
        sublist = []

        rows = len(board)
        cols = len(board[0]) # a single element of list board.  
        path = set()

        def dfs(r , c , i):

            if i == len(word):
                return True

            if r< 0 or c< 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r, c) in path:
                return False

            # what if it is the word, check all others
            

            path.add((r,c))
            res = dfs(r + 1, c,  i +1) or dfs(r-1, c , i +1) or dfs( r, c+1 , i +1 ) or dfs(r, c-1, i + 1)
            path.remove((r, c))
            return res
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0): 
                    return True
        return False


        