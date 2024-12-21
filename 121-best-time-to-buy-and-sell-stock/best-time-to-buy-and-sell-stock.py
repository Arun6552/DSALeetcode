class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Brute Foce approce
        maxi = 0
        diff = 0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                if prices[j] > prices[i] :
                    diff = prices[j]-prices[i]
                if diff > maxi:
                    maxi = diff
        return maxi

        '''
        maxProfit = 0 
        minValue  = prices[0]
        cost = 0
        for i in range(len(prices)):
            cost = prices[i] - minValue
            maxProfit = max(maxProfit,cost)
            minValue = min(minValue,prices[i])
        return maxProfit



        