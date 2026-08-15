class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rowlen = len(matrix)
        collen = len(matrix[0])

        l = 0
        r = (rowlen * collen) -1

        while l <= r:
            mid = (l+r)//2
            
            midrow = mid//collen
            midcol = mid % collen
            print(midcol, midrow)

            if matrix[midrow][midcol] == target:
                return True

            if matrix[midrow][midcol] > target:
                r = mid -1

            if matrix[midrow][midcol] < target:
                l = mid +1
        return False
            


        