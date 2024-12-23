class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        count = 0 
        row = len(matrix)
        for i in range(row):
            if target in matrix[i]:
                count +=1
        if count >=1:
            return True
        else:
            return False

           