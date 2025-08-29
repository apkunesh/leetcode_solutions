from heapq import heappush, heappop
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # MISTAKE 1: Missed that the graph is undirected (need to include both in and out for adjacency
        # map.)
        adj_map = defaultdict(set)
        for edge,success in zip(edges,succProb):
            source,dest = edge
            adj_map[source].add((success,dest))
            adj_map[dest].add((success,source))
        nodeheap = [(-1,start_node)]
        most_probable = {}
        # need to do maxheap instead
        while nodeheap:
            prob, node = heappop(nodeheap)
            prob = -prob
            if node in most_probable:
                continue
            if node == end_node:
                return prob
            most_probable[node] = prob
            neighbors = adj_map[node]
            for success,dest in neighbors:
                heappush(nodeheap,(-prob * success,dest))
        return 0