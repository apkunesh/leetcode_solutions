from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if n==1:
            return -1
        adj = defaultdict(list)
        for from_i,to_i,price_i in flights:
            adj[from_i].append([price_i,to_i])
        heap = [] 
        for new_price,new_dest in adj[src]:
            heappush(heap,(new_price,0,new_dest))
        visited_to_distance = {src:0}
        while heap:
            price,stops,dest = heappop(heap)
            if dest == dst:
                return price
            if k == stops:
                continue
            if dest in visited_to_distance and visited_to_distance[dest]>=stops:
                continue
            visited_to_distance[dest] = stops
            for new_price,new_dest in adj[dest]:
                heappush(heap,(price+new_price,stops+1,new_dest))
        return -1
