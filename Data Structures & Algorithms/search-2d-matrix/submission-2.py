class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rowlen = len(matrix)
        collen = len(matrix[0])

        l = 0
        r = (rowlen * collen) -1

        while l <= r:
            mid = (l+r)//2
            
            midcol = mid//collen
            midrow = mid % collen

            if matrix[midcol][midrow] == target:
                return True

            if matrix[midcol][midrow] > target:
                r = mid -1

            if matrix[midcol][midrow] < target:
                l = mid +1
        return False
            


        