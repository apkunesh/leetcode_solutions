from heapq import heapify, heappop

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #This is gonna be nlogn anyway, could be better to just sort up front.
        heapify(intervals)
        left,delete_count = heappop(intervals),0
        while intervals:
            candidate = heappop(intervals)
            if candidate[0] >= left[1]: #Happy case, they don't overlap
                left = candidate
                continue
            # So, they do overlap. Then we take the one which has the smallest right frontier
            left = left if candidate[1] > left[1] else candidate
            delete_count+=1
        return delete_count 