class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1  = 0 
        count2 = 0
        key1 = None
        key2 = None
        for i in range(len(nums)):
            if count1 ==0 and nums[i] != key2:
                count1 = 1
                key1 = nums[i]
            elif count2 ==0 and nums[i] != key1:
                count2 = 1
                key2= nums[i]
            elif key1 == nums[i]:
                count1 +=1
            elif key2 == nums[i]:
                count2 +=1
            else:
                count1 -=1
                count2 -=1
        cnt1 = 0 
        cnt2 = 0
        ans = []
        for i in range(len(nums)):
            if nums[i] ==key1:
                cnt1 +=1
            if nums[i] ==key2:
                cnt2 +=1
        if cnt1 > len(nums)//3:
            ans.append(key1)
        if cnt2 > len(nums)//3:
            ans.append(key2)
        return ans

      


            
                 
        
        