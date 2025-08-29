class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        has_inserted = False
        output=[]
        for interval in intervals:
            if interval[0] > newInterval[1] or interval[1] <newInterval[0]:
                if not has_inserted and interval[0] > newInterval[1]:
                    output.append(newInterval)
                    has_inserted = True
                output.append(interval)
                continue
            if not has_inserted:
                output.append([min(newInterval[0],interval[0]),max(newInterval[1],interval[1])])
                has_inserted = True
                continue
            output[-1][1] = max(output[-1][1],interval[1])
        if not has_inserted:
            output.append(newInterval)
        return output
