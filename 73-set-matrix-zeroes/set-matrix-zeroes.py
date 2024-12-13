class Solution:

    def setRows(self,matrix,r,c):
        for i in range(c):
            matrix[r][i] =0
        
    def setColumn(self,matrix,r,c):
        for i in range(r):
            matrix[i][c]=0


    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        r = len(matrix)
        c = len(matrix[0])
        viewMatrix = deepcopy(matrix)
        
        for i in range(r):
            for j in range(c):
                if viewMatrix[i][j] ==0:
                    self.setRows(matrix,i,c)
                    self.setColumn(matrix,r,j)
        

        