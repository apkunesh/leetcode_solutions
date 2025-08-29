class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        output = [intervals[0]]
        for i in range(1,len(intervals)):
            tentative = intervals[i]
            if tentative[0] <= output[-1][1]:
                output[-1][1] = max(tentative[1],output[-1][1])
            else:
                output.append(tentative)
        return output