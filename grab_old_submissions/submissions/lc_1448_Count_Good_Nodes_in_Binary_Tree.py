"""
Miss was just a difference in Neetcode and Leetcode -- ranges in Neetcode are -100 to 100, whereas Leetcode
are between -10**4 and 10**4
"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        path_max,node_stack,node,good_count = -1000000,[(root,-1000000)], None,0
        while node_stack or node:
            if node is None:
                node,path_max = node_stack.pop()
            else:
                if node.val >= path_max:
                    good_count+=1
                path_max = max(node.val,path_max)
                node_stack.append((node.right,path_max))
                node = node.left
        return good_count
