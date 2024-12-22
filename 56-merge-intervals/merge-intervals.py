class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        Optimal Solution 
        '''
        result = []
        intervals.sort()
        for i in range(len(intervals)):
            if not result or  intervals[i][0] > result[-1][1]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(result[-1][1],intervals[i][1])
        return result
        