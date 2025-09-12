from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        result = ["JFK"]

        def dfs(src):
            if adj[src] == [] and len(result) == len(tickets) + 1:
                return result
            cur_level_copy = adj[src].copy()
            for i in range(len(cur_level_copy)):
                elem = adj[src].pop(i)
                result.append(elem)
                maybe_results = dfs(elem)
                if maybe_results:
                    return maybe_results
                result.pop()
                adj[src].insert(i, elem)
            return None

        grand_result = dfs("JFK")
        return grand_result
