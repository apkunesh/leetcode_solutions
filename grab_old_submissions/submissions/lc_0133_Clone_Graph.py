"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # Pretty harrowing. Note that the desired return type is Node, not
    # a list of list of int. Fuck.
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        adj_map = {}
        queue = deque()
        queue.append(node)
        seen = set([node])
        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.popleft()
                seen.add(curr)
                if adj_map.get(curr.val) is None:
                    adj_map[curr.val] = set([elem.val for elem in curr.neighbors])
                else:
                    for elem in curr.neighbors:
                        adj_map[curr.val].add(elem.val)
                for neighbor in curr.neighbors:
                    if adj_map.get(neighbor.val) is None:
                        adj_map[neighbor.val] = set([curr.val])
                    else:
                        adj_map[neighbor.val].add(curr.val)
                for neighbor in curr.neighbors:
                    if neighbor not in seen:
                        queue.append(neighbor)
                        seen.add(neighbor)
        def spawn_nodes(node_val,neighbor_vals,already_generated,adj_list):
            if node_val in already_generated:
                return already_generated[node_val]
            new_node = Node(node_val)
            already_generated[node_val] = new_node
            children = [spawn_nodes(val,adj_list[val],already_generated,adj_list) for val in neighbor_vals if val]
            children = [child for child in children if child is not None]
            new_node.neighbors = children
            return new_node

        result =  spawn_nodes(1,adj_map[1],{},adj_map)
        return result