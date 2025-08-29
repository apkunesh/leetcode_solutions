class SegmentMaxNode:
    def __init__(self,L,R):
        self.L = L
        self.R = R
        self.left = None
        self.right = None
        self.max = 0
    
    def add_leaf(self,num):
        if self.L == self.R:
            return # Leaf already present
        middle = (self.L+self.R)//2
        if num > middle:
            if not self.right:
                self.right = SegmentMaxNode(middle+1,self.R)
            self.right.add_leaf(num)
        else:
            if not self.left:
                self.left = SegmentMaxNode(self.L,middle)
            self.left.add_leaf(num)
 
    def update(self,index,val):
        if self.L == self.R: # Case 1: we're at a leaf which already exists
            if self.L == index:
                self.max = val
                return
        middle = (self.L+self.R)//2
        if index > middle:
            self.right.update(index,val)
        else:
            self.left.update(index,val)
        left_max = self.left.max if self.left else 0
        right_max = self.right.max if self.right else 0
        self.max = max(left_max,right_max)
    
    def query_range(self,L,R):
        if L == self.L and R == self.R:
            return self.max
        middle = (self.L + self.R)//2
        if R<middle:
            if not self.left:
                return 0
            return self.left.query_range(L,R)
        elif L>middle:
            if not self.right:
                return 0
            return self.right.query_range(L,R)
        else:
            left_range = self.left.query_range(L,middle) if self.left else 0
            right_range = self.right.query_range(middle+1,R) if self.right else 0
            return max(left_range,right_range)


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        # ERR 1: Made the mistake of trying to do analysis on the full array (using a hashset from the full array) instead of treating the problem as "time-asymmetric": only neighbors to the right matter, ex.
        # ERR 2: My new soln had the same pathological issue of checking all k parents for every node. I now will update a segment tree on which I can do range queries for the max to that point based on a number (not an index) and traverse the list from left-to-right
        # DEBUG 3: In the seemingly-correct soln, missed the base case of QueryRange: where L = self.L and R = self.R. We'll initialize a bunch of segment nodes with all the nums
        # ERR 3: Failed to initialize the tree to encompass the whole range of queryable values (min(nums)-k)
        root = SegmentMaxNode(min(nums)-k-2,max(nums))
        for num in nums:
            root.add_leaf(num)
        for i in range(len(nums)):
            cur = nums[i]
            max_parents = root.query_range(cur-k,cur-1)
            root.update(cur,max_parents+1)
        return root.max
