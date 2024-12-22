class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        low = 1
        high = len(nums)-1
        while (low < high) :
            mid = (low + high)//2
            count = 0 
            for num in nums: 
                if num <= mid:
                    count +=1
            if count > mid: 
                high = mid
            else: 
                low = mid+1
            
        return low
       
 

        


        '''
        Brute Force Sol
            ans = []
            for i in nums:
                if i in ans:
                    return i 
                else: 
                    ans.append(i) 

        nums.sort()
        for i in range(len(nums)+1):
            if nums[i] == nums[i+1]:
                return nums[i]

               
        hashnum = [0]* len(nums)
        for i in nums:
            if hashnum[i] != 1:
                hashnum[i]=1
            else:
                return i 
        '''
        
      