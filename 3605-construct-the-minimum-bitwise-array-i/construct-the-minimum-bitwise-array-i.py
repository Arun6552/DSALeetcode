class Solution:
    def minBitwiseArray(self, nums):
        ans = []

        for x in nums:
            # Even numbers are impossible
            if x % 2 == 0:
                ans.append(-1)
                continue

            # Count trailing 1s
            k = 0
            temp = x
            while temp & 1:
                k += 1
                temp >>= 1

            # Minimum valid ans
            ans.append(x - (1 << (k - 1)))

        return ans
