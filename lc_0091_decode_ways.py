"""
'A' -> "1"
'B' -> "2"
'Z' -> "26"

"""

from typing import Optional

# Improve this by caching on i+candidate.


class Solution:
    def numDecodings(self, s: str) -> int:
        candidate_position_cache = {}

        def recurse(i, prev_num: Optional[int] = None):
            candidate = 10 * prev_num + int(s[i]) if prev_num is not None else int(s[i])
            if candidate < 1 or candidate > 26:
                return 0  # a valid str
            if i == len(s) - 1:
                return 1
            if (i, candidate) in candidate_position_cache:
                return candidate_position_cache[(i, candidate)]
            ways = 0
            ways += recurse(i + 1, candidate)
            ways += recurse(i + 1)
            candidate_position_cache[(i, candidate)] = ways
            return candidate_position_cache[(i, candidate)]

        return recurse(0)
