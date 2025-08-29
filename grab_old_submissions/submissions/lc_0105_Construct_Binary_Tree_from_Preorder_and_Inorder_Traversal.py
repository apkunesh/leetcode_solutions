# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Holy shit so many mistakes along the way. NEed to eat I think.
        # Biggest error was attempting to apply binary search on unordered lists.

        # Basic idea:
        # Scan across pre-order. The first should be the whole tree root.
        # For subsequent entries: is this to the left or right of the parent
        # inorder?

        # This should take nlogn time, since we traverse the list 1 time and 
        # traverse the tree we're building for each new node, which should take approx
        # log n 
        base_node = TreeNode(val=preorder[0])
        inorder_val_to_index = {inorder[i] : i for i in range(len(inorder))}
        for i in range(len(preorder)-1):
            preorder_index = i+1
            comparison_node = base_node
            found = False
            while not found:
                comparison_node_index = inorder_val_to_index[comparison_node.val]
                insertion_node_index = inorder_val_to_index[preorder[preorder_index]]
                if insertion_node_index < comparison_node_index:
                    if not comparison_node.left:
                        comparison_node.left = TreeNode(val=preorder[preorder_index])
                        found = True
                    else:
                        comparison_node = comparison_node.left
                elif insertion_node_index > comparison_node_index:
                    if not comparison_node.right:
                        comparison_node.right = TreeNode(val=preorder[preorder_index])
                        found = True
                    else:
                        comparison_node = comparison_node.right
        return base_node