"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Idea: DFS on randoms, with a hashmap from id of the original node
        # to new nodes

        def dfs(node,hashmap):
            if node is None:
                return None
            if id(node) in hashmap:
                return hashmap[id(node)]
            hashmap[id(node)] = Node(x=node.val)
            hashmap[id(node)].next = dfs(node.next,hashmap)
            if node.random==node:
                hashmap[id(node)].random = hashmap[id(node)]
            else:
                hashmap[id(node)].random = dfs(node.random,hashmap)
            return hashmap[id(node)]

        return dfs(head,{})
