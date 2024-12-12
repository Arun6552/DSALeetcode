class Solution:

    def  setRows(self,matrix,row,column):
        for i in range(column):
            matrix[row][i]=0
    def setColumns(self,matrix,row,column):
        for i in range(row):
            matrix[i][column]=0
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
       

        row = len(matrix)
        column = len(matrix[0])
        #viewMatrix = deepcopy(matrix)
        viewMatrix = [[matrix[i][j] for j in range(column)] for i in range(row)]
       
        for i in range(row):
            for j in range(column):
                if viewMatrix[i][j] ==0:
                    self.setRows(matrix,i,column)
                    self.setColumns(matrix,row,j)
       
        