# NOTE: Couldn't do this on first try after about an hour. Will loop back to it.

from typing import List


class IntervalTree():
    def __init__(self,L,R):
        self.L = L
        self.R = R
        self.interval_len = -1
        self.left = None
        self.right = None
    def spawn_children(self,L,R,range_l,range_r): 
        new_child = IntervalTree(L,R)
        if L >= range_l and R <= range_r:
            new_child.interval_len = range_r - range_l
            return new_child
        else:
            middle = (L+R)//2
            if range_l < middle:
                new_child.left = self.spawn_children(L,middle,range_l,range_r)
            if range_r > middle:
                new_child.right = self.spawn_children(middle+1,R,range_l,range_r)
    def update(self,L,R, child_l, child_r):
        if not self.L and not self.R:
            # Basically, recurse down; for any areas where 
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        base_interval = IntervalTree(0,10001)
        base_interval.interval_len = -1
        # We'll sort by minimum length first


        return []

