from collections import defaultdict
from heapq import heapify, heappop, heappush
from typing import List


class Graph:
    """
    High-level, the question is: how can we efficiently compute shortest distances between nodes, particularly with the addition and deletion of edges?
    Obviously we have greedy algorithms (Djikstra's), but it seems like there's a bunch of repeat work.
    Perhaps what we can do is:
    - If there are no new edges, recycle the old "minimum cost" matrix. This is a cheap optimization.
    - If there *are* new edges, we can retain our old cost matrix if the newly-established cost between the two points is the same or greather than before. Otherwise, let's flush it for now. It may be possible to retain components in the future if we have some path-specific info, but -- particularly for minima whose paths do not use this edge -- I don't think we can avoid Djikstras or similar.
    """

    def __init__(self, n: int, edges: List[List[int]]):
        self.adj = defaultdict(list)
        self.min_cost = {}
        for edge in edges:
            self.adj[edge[0]].append((edge[2], edge[1]))

    def addEdge(self, edge: List[int]) -> None:
        if self.shortestPath(edge[0], edge[1]) > edge[2]:
            self.min_cost = {}
        self.adj[edge[0]].append((edge[2], edge[1]))
        # TODO: Dump min_cost cache if this shortens the path

    def shortestPath(self, node1: int, node2: int) -> int:
        if node1 == node2:
            return 0
        if (node1, node2) in self.min_cost:
            return self.min_cost[(node1, node2)]
        seen = set()
        frontier = self.adj[node1].copy()
        heapify(frontier)
        while frontier:
            cost, dest = heappop(frontier)
            seen.add(dest)
            if dest == node2:
                self.min_cost[(node1, node2)] = cost
                return self.min_cost[(node1, node2)]
            for new_cost, new_dest in self.adj[dest]:
                if new_dest not in seen:
                    heappush(frontier, (cost + new_cost, new_dest))

        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
