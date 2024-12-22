class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)+1):
            if nums[i] == nums[i+1]:
                return nums[i]

        '''
        Brute Force Sol
            ans = []
            for i in nums:
                if i in ans:
                    return i 
                else: 
                    ans.append(i) 
        '''
        
      