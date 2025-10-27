from collections import deque
from heapq import heappop, heappush
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1
        min_heap, node_level = [], deque([root])
        while node_level:
            local_sum = 0
            for _ in range(len(node_level)):
                cur_node = node_level.popleft()
                local_sum += cur_node.val
                if cur_node.left:
                    node_level.append(cur_node.left)
                if cur_node.right:
                    node_level.append(cur_node.right)
            if len(min_heap) < k or local_sum > min_heap[0]:
                heappush(min_heap, local_sum)
            if len(min_heap) > k:
                heappop(min_heap)
        if len(min_heap) < k:
            return -1
        return min_heap[0]  # type: ignore`<F11>


def construct_tree(values_in: List[Optional[int]]):
    base_node = TreeNode(val=values_in[0])  # type: ignore
    prev_level = [base_node]
    start = 1
    end = 3  # Exclusive
    while start < len(values_in):
        new_level = []
        for i in range(end - start):
            parent_index = i // 2
            if (
                parent_index >= len(prev_level)
                or prev_level[parent_index] is None
                or start + i >= len(values_in)
            ):
                continue
            if i % 2 == 0:
                if values_in[start + i] is not None:
                    prev_level[parent_index].left = TreeNode(values_in[start + i])
                new_level.append(prev_level[parent_index].left)
            if i % 2 == 1:
                if values_in[start + i] is not None:
                    prev_level[parent_index].right = TreeNode(values_in[start + i])
                new_level.append(prev_level[parent_index].right)
        # print(
        #     f"Previous level included {[elem.val if elem is not None else None for elem in prev_level]}"
        # )
        prev_level = new_level
        old_end = end
        end = end + 2 * (end - start)
        start = old_end
    return base_node


def print_tree(node):
    if node is None:
        return
    print(
        f'{node.val} has children {node.left.val if node.left else "none"} and {node.right.val if node.right else "none"}'
    )
    print_tree(node.left)
    print_tree(node.right)


ex_1 = construct_tree([5, 8, 9, 2, 1, 3, 7, 4, 6])
ex_2 = construct_tree([1, 2, None, 3])
ex_3 = construct_tree([1])
# print_tree(ex_1)
soln = Solution().kthLargestLevelSum
print(f"{soln(ex_1, 2)} should be 13")
print(f"{soln(ex_2, 1)} should be 3")
print(f"{soln(ex_3, 2)} should be -1")

"""
Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13

Input: root = [1,2,null,3], k = 1
Output: 3

 
    The number of nodes in the tree is n.
    2 <= n <= 105
    1 <= Node.val <= 106
    1 <= k <= n
"""
