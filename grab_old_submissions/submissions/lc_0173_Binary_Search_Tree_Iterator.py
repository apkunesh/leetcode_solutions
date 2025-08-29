# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.cur = root

    def next(self) -> int:
        while self.cur or self.stack:
            if self.cur:
                self.stack.append(self.cur)
                self.cur = self.cur.left
            else:
                self.cur = self.stack.pop()
                dummy = self.cur.val
                self.cur = self.cur.right
                return dummy
        
    def hasNext(self) -> bool:
        return False if not (self.cur or self.stack) else True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()