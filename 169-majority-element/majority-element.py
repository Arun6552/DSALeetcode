class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count  = 0 
        key = None
        for i in range(len(nums)):
            if count ==0:
                count = 1
                key = nums[i]
            elif key == nums[i]:
                count +=1
            else:
                count -=1
        count1 = 0 
        for i in range(len(nums)):
            if nums[i] ==key:
                count1 +=1
        if count1 > len(nums)//2:
            return key
        else:
            return -1

      


            
                 
        