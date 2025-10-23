from collections import defaultdict
from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        sequence_map, grand_max = defaultdict(dict), 2
        for i in range(1, len(nums)):
            cand = nums[i]
            if cand in sequence_map:
                to_update = sequence_map.pop(cand)
                for delta, count in to_update.items():
                    local_max = count + 1
                    sequence_map[cand + delta][delta] = max(
                        [local_max, sequence_map[cand + delta].get(delta) or 2]
                    )
                    grand_max = max([grand_max, local_max])
            for j in range(0, i):
                delta = cand - nums[j]
                sequence_map[cand + delta][delta] = (
                    sequence_map[cand + delta].get(delta) or 2
                )
        return grand_max


soln = Solution().longestArithSeqLength
print(f"{soln([3, 6, 9, 12])} should be 4")
print(f"{soln([9, 4, 7, 2, 10])} should be 3")
print(f"{soln([20, 1, 15, 3, 10, 5, 8])} should be 4")
