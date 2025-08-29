class Node():
    def __init__(self,val):
        self.val = val
        self.children = []
        self.path_len = None

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        index_to_node = {}
        for i in range(len(nums)):
            node_here = Node(nums[i])
            for node in index_to_node.values():
                if node.val < node_here.val:
                    node.children.append(node_here)
            index_to_node[i] = node_here
        global_max_length = 1
        for i in range(len(nums)-1,-1,-1):
            children_here = index_to_node[i].children
            index_to_node[i].path_len = 1 if children_here == [] else max([elem.path_len for elem in children_here]) + 1
            global_max_length = max(global_max_length,index_to_node[i].path_len)
        return global_max_length

