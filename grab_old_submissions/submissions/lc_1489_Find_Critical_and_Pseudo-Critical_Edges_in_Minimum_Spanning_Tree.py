from heapq import heappush,heappop

def union(node_1,node_2):
    root_1,root_2 = node_1.find(),node_2.find()
    if root_1 == root_2:
        return False
    if root_1.rank > root_2.rank:
        root_2.parent = root_1
    elif root_2.rank > root_1.rank:
        root_1.parent = root_2
    else:
        root_1.rank +=1
        root_2.parent = root_1

class UnionNode():
    def __init__(self):
        self.parent = self
        self.rank = 1

    def find(self):
        if self.parent !=self:
            self.parent = self.parent.find()
        return self.parent

def kruskals(edges,n,int_to_node = None,total_weight = None, disallowed=None): # disallowed is an int
    if int_to_node is None:
        int_to_node = {i:UnionNode() for i in range(n)}
        points_included = 1
        total_weight = 0
    else:
        points_included = 2
    edge_heap = []
    for edge,edge_id in zip(edges,range(len(edges))):
        if edge_id == disallowed:
            continue
        heappush(edge_heap,(edge[2],edge[0],edge[1],edge_id))
    while edge_heap:
        weight,node_1,node_2,edge_id = heappop(edge_heap)
        node_1,node_2 = int_to_node[node_1],int_to_node[node_2]
        new_connection = union(node_1,node_2)
        if new_connection is False:
            continue
        total_weight += weight
        points_included+=1
        if points_included == n:
            return total_weight
    return -50000

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Big idea: 
        #    1) find base weight (no restrictions)
        #    2) find critical edges (removing increases weight or makes construction impossible)
        #    3) find pseudo-critical edges (force-adding them does not increase weight)
        # This time we'll solve with Kruskal's
        base_weight = kruskals(edges,n)
        critical = []
        for i in range(len(edges)):
            critical_weight = kruskals(edges,n,disallowed = i)
            if critical_weight > base_weight or critical_weight == -50000:
                critical.append(i)
        pseudo_critical = []
        for edge,edge_id in zip(edges,range(len(edges))):
            if edge_id in critical:
                continue
            int_to_node = {i:UnionNode() for i in range(n)}
            union(int_to_node[edge[0]],int_to_node[edge[1]])
            total_weight = edge[2]
            pseudo_critical_weight = kruskals(edges,n,int_to_node = int_to_node,total_weight = edge[2])
            if pseudo_critical_weight == base_weight:
                pseudo_critical.append(edge_id)
        return [critical,pseudo_critical]