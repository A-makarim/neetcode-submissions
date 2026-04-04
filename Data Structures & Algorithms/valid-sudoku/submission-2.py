# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         rowexists = set()
#         colexists = set()
#         boxexists = set()

#         for i in range(9):
#             for j in range(9):
#                 if board[i][j] == ".":
#                     continue
#                 col = ("col", j, board[i][j])
#                 row = ("row", i, board[i][j])
#                 box  = ("box", i//3, j//3 , board[i][j])
#                 if col not in colexists and row not in rowexists and box not in boxexists:
#                     colexists.add(col)
#                     rowexists.add(row)
#                     boxexists.add(box)

#                 else:

#                     return False
#         return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowexists = defaultdict(set)
        colexists = defaultdict(set)
        boxexists = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in rowexists[i] and board[i][j] not in colexists[j] and board[i][j] not in boxexists[(i//3), (j//3)]:
                     colexists[j].add(board[i][j])
                     rowexists[i].add(board[i][j])
                     boxexists[(i//3), (j//3)].add(board[i][j])
                else:
                    return False
        return True






