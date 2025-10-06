from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Idea: Just do an in-order traversal (TC: O(log(n) + k), or similar) and stop at the kth element.
        """
        # But how does an element know which one it is?
        # Let's modify a global variable with the count. Between checking left and right, we'll update this variable.
        found_index = {"ind": 0}

        def recurse(node: Optional[TreeNode]):
            if node is None:
                return
            left_result = recurse(node.left)
            if left_result is not None:
                return left_result
            found_index["ind"] = found_index["ind"] + 1
            if found_index["ind"] == k:
                return node.val
            right_result = recurse(node.right)
            if right_result is not None:
                return right_result

        grand_result = recurse(root)
        return grand_result  # type: ignore


def create_tree(list_in, i):
    if i >= len(list_in) or list_in[i] is None:
        return None
    this_node = TreeNode(
        val=list_in[i],
        left=create_tree(list_in, 2 * i + 1),
        right=create_tree(list_in, 2 * i + 2),
    )
    return this_node


print(f"{Solution().kthSmallest(create_tree([3,1,4,None,2],0),1)} should be 1")
print(f"{Solution().kthSmallest(create_tree([5,3,6,2,4,None,None,1],0),3)} should be 3")


"""
Input: root = [3,1,4,null,2], k = 1
Output: 1


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""

