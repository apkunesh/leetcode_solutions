from collections import defaultdict, deque
from typing import List


class Solution:
    # NOTE: To make this not TLE, instead of finding all paths, I think I should instead the number of paths from any node to all other nodes *except* some set of nodes. This is sorta DP, and avoids retracing duplicate paths.
    # What's the TC of constructing this?
    # The number of such exclusion sets is 2^14 -> 16384
    # The number of traversals I might have to do for each could be large: V**2 potentital edges
    # NOTE: Okay, I think I have a concept, though implementation is difficult. I want to spend a little time on complexity analysis.
    # For any component of the graph with n elements, we can construct a mapping from component elements to the number of paths which hit every other element within the component. So, given 3 elements a b c, we can assign a number to a, b, c such that the resulting number of distinct paths covering that component are the sum of these numbers.
    # We can build this up until our component of interest is the full graph.
    def specialPerm(self, nums: List[int]) -> int:
        adj, n = defaultdict(set), len(nums)
        last_layer = deque()
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    adj[nums[i]].add(nums[j])
                    adj[nums[j]].add(nums[i])
                    key = [nums[i], nums[j]]
                    last_layer.append([set(key), 1])
        while last_layer:
            for _ in range(len(last_layer)):
                visited, pathcount = last_layer.popleft()
                for new_start in nums:
                    if new_start in visited:
                        continue
                    new_pathcount = 0
                    for lil_start in visited:
                        if lil_start in adj[new_start]:
                            new_pathcount += pathcount


print(f"{Solution().specialPerm([2,3,6])}")  # 2
print(f"{Solution().specialPerm([1,4,3])}")  # 2
