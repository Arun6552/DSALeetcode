class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Optimal Solution 
        num_map = {}
        for i in range(len(nums)):
            num = nums[i]
            requiredNum = target - num
            if requiredNum in num_map:
                return [num_map[requiredNum], i]
            
            num_map[num] = i


    
    '''
     Brute Force Solution 
        result = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    result.append(i)
                    result.append(j)
        return result
    '''
   
       



        