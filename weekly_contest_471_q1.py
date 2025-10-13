from typing import List
from collections import defaultdict


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        countmap = defaultdict(int)
        for elem in nums:
            countmap[elem] += 1
        grand_result = 0
        for key, val in countmap.items():
            if val % k == 0:
                grand_result += key * val
        return grand_result
