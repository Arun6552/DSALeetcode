class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #1st Better approach counting 0's,1's,2's.
        '''
        count0 =0
        count1=0
        count2 =0

        for i in range(len(nums)):
            if nums[i] == 0 : 
                count0 += 1
            if nums[i] == 1:
                count1 += 1
            if nums[i] ==2 :
                count2 += 1

        for i in range(count0):
            nums[i] = 0
        for i in range(count0,count0+count1):
            nums[i] = 1
        for i in range(count0+count1,len(nums)):
            nums[i] = 2
        '''
        low =0
        mid = 0
        high = len(nums)-1
        while (mid <= high):
            if nums[mid] == 0:
                nums[low],nums[mid]  = nums[mid],nums[low]
                low +=1
                mid +=1
            elif nums[mid] ==1:
                mid +=1 
            else:
                nums[mid],nums[high]  = nums[high],nums[mid]
                high -=1 


            










    
       
    
        