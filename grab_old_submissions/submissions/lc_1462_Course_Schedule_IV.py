# Idea 1: create topological sort -> a dict mapping the course to its position. Comparison of the positions of two courses will yield prereq order.
# Rebuttal 1: This solution does not adequately handle unrelated courses.
# Idea 2: Construct the adjacency matrix -> do UnionFind to construct components -> do topological sort on each component. Map each component's root to the associated top sort. For each query, check if they are in the same component; if yes, check if they are prerequisities on the associated top sort; else return false.
# This will work, but is it ideal? Unionfind will be O(n*log(n)) to construct, I believe, and topological sort will be O(N)

# First major mistake involved the union find: we union roots, not just the original nodes.
# ERROR 1: Building topological orderings doesn't adequately capture when things are *not* prereqs. 
# Consider a -> c <- b. A and B do not have a prereq relationship, but a topological ordering may reveal one nonetheless.

# So, let's start with the naive solution (DFS) and see what optimizations we can make.
from collections import defaultdict

def dfs(adj,val_1,val_2):
    if val_2 in adj[val_1]:
        return True
    for child in adj[val_1]:
        if dfs(adj,child,val_2) is True:
            return True
    return False

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(set)
        for prereq,course in prerequisites:
            adj[prereq].add(course)
        answer = []
        for a,b in queries:
            answer.append(dfs(adj,a,b))
        return answer