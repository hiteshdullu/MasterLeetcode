class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        for row in range(rows):
            i = 0
            j = len(matrix[0])-1
            if matrix[row][i] <= target and matrix[row][j] >= target:
                while i <= j:
                    mid = (i+j)//2
                    if matrix[row][mid] == target:
                        return True
                    elif matrix[row][mid] < target:
                        i = mid+1
                    else:
                        j = mid-1
        return False
