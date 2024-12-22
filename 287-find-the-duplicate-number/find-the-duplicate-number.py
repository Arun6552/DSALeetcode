class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       

        hashnum = [0]* len(nums)
        for i in nums:
            if hashnum[i] != 1:
                hashnum[i]=1
            else:
                return i 


        '''
        Brute Force Sol
            ans = []
            for i in nums:
                if i in ans:
                    return i 
                else: 
                    ans.append(i) 
        '''
        
      