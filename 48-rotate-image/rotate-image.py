class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix = self.transpose(matrix)
  
    def transpose(self,matrix):
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        self.rowReverse(matrix)
        return matrix

    def rowReverse(self,matrix):
        row = len(matrix)
        for i in range(row):
            matrix[i] = matrix[i][::-1]

   
        
       
        