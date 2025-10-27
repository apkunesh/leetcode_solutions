from collections import defaultdict
from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        safe = defaultdict(dict)
        mineset = set([(elem[1], elem[0]) for elem in mines])
        for r in range(n):
            for c in range(n):
                if (r, c) in mineset:
                    safe[(r, c)]["l"] = 0
                    safe[(r, c)]["r"] = 0
                    safe[(r, c)]["u"] = 0
                    safe[(r, c)]["d"] = 0
                else:
                    left_safe = safe[(r, c - 1)]["l"] if c - 1 >= 0 else 0
                    up_safe = safe[(r - 1, c)]["u"] if r - 1 >= 0 else 0
                    safe[(r, c)]["l"] = left_safe + 1
                    safe[(r, c)]["u"] = up_safe + 1
        order = 0
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if (r, c) in mineset:
                    continue
                else:
                    right_safe = safe[(r, c + 1)]["r"] if c + 1 < n else 0
                    down_safe = safe[(r + 1, c)]["d"] if r + 1 < n else 0
                    safe[(r, c)]["r"] = right_safe + 1
                    safe[(r, c)]["d"] = down_safe + 1
                entry = safe[(r, c)]
                local_order = min([entry["r"], entry["l"], entry["u"], entry["d"]])
                order = max(local_order, order)
        return order


soln = Solution().orderOfLargestPlusSign
print(f"{soln(5,[[4,2]])} should be 2")
print(f"{soln(1,[[0,0]])} should be 0")
