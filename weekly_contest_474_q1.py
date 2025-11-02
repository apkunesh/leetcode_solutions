from typing import List, Optional


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        minimum, maximum = min(nums), max(nums)
        all_nums = set(nums)
        result = []
        for i in range(minimum, maximum):
            if i not in all_nums:
                result.append(i)
        return result
