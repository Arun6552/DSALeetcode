from typing import List

class Solution:
    def swapNum(self, breakPointNum, nums):
        """
        Swap the number at the breakpoint with the closest higher number.
        """
        # Find the smallest number greater than nums[breakPointNum]
        for i in range(len(nums) - 1, breakPointNum, -1):
            if nums[i] > nums[breakPointNum]:
                nums[i], nums[breakPointNum] = nums[breakPointNum], nums[i]
                break
        return nums

    def reverse(self, breakPointNum, nums):
        """
        Reverse the portion of the array after the breakpoint index.
        """
        nums[breakPointNum + 1:] = nums[breakPointNum + 1:][::-1]
        return nums

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modify nums in-place to the next lexicographical permutation.
        If no such permutation exists, rearrange nums into the lowest order.
        """
        n = len(nums)
        breakPointNum = -1

        # Step 1: Find the breakpoint (first number smaller than its next from the end)
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                breakPointNum = i
                break

        # Step 2: If no breakpoint is found, reverse the entire array
        if breakPointNum == -1:
            nums.reverse()
            return

        # Step 3: Swap the breakpoint number with the next closest larger number
        self.swapNum(breakPointNum, nums)

        # Step 4: Reverse the portion after the breakpoint
        self.reverse(breakPointNum, nums)
