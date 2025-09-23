from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        result_cache = {}

        def recurse(l, r, cut_l, cut_r):
            if (l, r) in result_cache:
                return result_cache[(l, r)]
            if cut_r < cut_l:
                return 0
            elif cut_l == cut_r:
                result_cache[(l, r)] = r - l
                return result_cache[(l, r)]
            else:
                local_results = []
                for cut_ind in range(cut_l, cut_r + 1):
                    left_range = (l, cuts[cut_ind])
                    right_range = (cuts[cut_ind], r)
                    result = (
                        r
                        - l
                        + recurse(left_range[0], left_range[1], cut_l, cut_ind - 1)
                        + recurse(right_range[0], right_range[1], cut_ind + 1, cut_r)
                    )
                    local_results.append(result)
                grand_result = min(local_results)
                result_cache[(l, r)] = grand_result
                return result_cache[(l, r)]

        return recurse(0, n, 0, len(cuts) - 1)
