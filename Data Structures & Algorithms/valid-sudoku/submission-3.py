class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        colexist = defaultdict(list)

        rowexist = defaultdict(list)
        boxexist = defaultdict(list)  
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in colexist[j] and board[i][j] not in rowexist[i] and board[i][j] not in boxexist[(i//3, j//3)]:

                    colexist[j].append(board[i][j])
                    rowexist[i].append(board[i][j])
                    boxexist[(i//3, j//3)].append(board[i][j])
                else:
                    return False
        return True 

        
    
