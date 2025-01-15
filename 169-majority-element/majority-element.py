class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res,maxCount = 0,0 
        for num in nums:
            count[num] = 1 + count.get(num,0)
            res = num if count[num] > maxCount else res
            maxCount = max(count[num],maxCount)
        return res

       


        
       
        