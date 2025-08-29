class SegmentNode:
    def __init__(self,nums,L,R):
        self.L = L
        self.R = R
        if self.L == self.R:
            self.left = None
            self.right = None
            self.val = nums[L]
            return
        middle = (L+R)//2
        self.left = SegmentNode(nums,L,middle)
        self.right = SegmentNode(nums,middle+1,R)
        self.val = self.left.val + self.right.val
    
    def update(self,index,val):
        if self.L == self.R: #We're at a leaf
            if index == self.L:
                self.val = val
                return self
            else:
                print("Somehow we've pathed to the wrong node, "+str(self.L)+" given input index " + str(index))
                return self # In this bad case we do nothing
        middle = (self.L+self.R)//2
        if middle >= index:
            self.left = self.left.update(index,val)
        elif middle < index:
            self.right = self.right.update(index,val)
        self.val = self.left.val + self.right.val
        return self

    def range_query(self,L,R):
        if self.L == L and self.R == R:
            return self.val
        middle = (self.L+self.R)//2
        if L>middle:
            return self.right.range_query(L,R)
        elif R<=middle:
            return self.left.range_query(L,R)
        else:
            return self.left.range_query(L,middle) + self.right.range_query(middle+1,R)

class NumArray:

    def __init__(self, nums: List[int]):
        self.head = SegmentNode(nums,0,len(nums)-1)

    def update(self, index: int, val: int) -> None:
        self.head.update(index,val)

    def sumRange(self, left: int, right: int) -> int:
        return self.head.range_query(left,right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)