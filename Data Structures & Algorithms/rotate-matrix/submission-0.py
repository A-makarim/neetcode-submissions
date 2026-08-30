class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        lenrow = len(matrix)
        lencol = len(matrix[0])

        for r in range(lenrow):
            for c in range(r + 1, lencol):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        for i in matrix:
            i.reverse()

        return