class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Index for the next position to keep valid elements
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Overwrite the value at index k
                k += 1
        return k
