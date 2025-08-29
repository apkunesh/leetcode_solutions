class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Given p and q, one is greater than the other.
        Thus, there are two cases for the lowest common ancestor:
         - That ancestor *is* p or q, and q or p is a descendent
         - That ancestor *is between* p and q, and p and q are contained in its left and right subtrees.
        """
        small = p if p.val<q.val else q
        large = q if p.val<q.val else p
        while root:
            if root.val == p.val or root.val == q.val:
                return root
            if root.val > small.val and root.val < large.val:
                return root
            if root.val > large.val:
                root = root.left
            elif root.val < small.val:
                root = root.right
            else:
                raise Exception("not accessible")
        