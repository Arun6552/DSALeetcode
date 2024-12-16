class Solution:

    def nCr(self,n,r):
        res = 1
        for i in range (r):
            res = res *(n-i)
            res = res//(i+1)
        return (int(res))

    def generate(self, numRows: int) -> List[List[int]]:
        ans= []
        for row in range(1,numRows+1):
            listRows=[]
            for col in range(1,row+1):
                listRows.append(self.nCr(row-1,col-1))
            ans.append(listRows)
        return ans
        