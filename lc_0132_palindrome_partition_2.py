from collections import defaultdict


class Solution:
    def minCut(self, s: str) -> int:
        is_palindrome, left_palis = set(), defaultdict(set)
        for i in range(len(s)):
            rad = 0
            while i + rad < len(s) and i - rad >= 0 and s[i + rad] == s[i - rad]:
                is_palindrome.add((i - rad, i + rad))
                left_palis[i + rad].add(i - rad)
                rad += 1
        for left, right in zip(range(0, len(s) - 1), range(1, len(s))):
            rad = 0
            while (
                left - rad >= 0
                and right + rad < len(s)
                and s[left - rad] == s[right + rad]
            ):
                is_palindrome.add((left - rad, right + rad))
                left_palis[right + rad].add(left - rad)
                rad += 1
        min_partition_cache = {}

        def min_partitions_between_indices(i, j) -> int:
            if (i, j) in min_partition_cache:
                return min_partition_cache[(i, j)]
            if (i, j) in is_palindrome:
                min_partition_cache[(i, j)] = 0
                return min_partition_cache[(i, j)]
            local_min = 10**30
            for left in left_palis[j]:
                local_min = (
                    min(
                        local_min,
                        min_partitions_between_indices(i, left - 1) + 1,
                    )
                    if left > i
                    else 0
                )
            min_partition_cache[(i, j)] = local_min
            return min_partition_cache[(i, j)]

        result = min_partitions_between_indices(0, len(s) - 1)
        return result


print(Solution().minCut("aab") == 1)
print(Solution().minCut("a") == 0)
print(Solution().minCut("ab") == 1)
print(f'{Solution().minCut("dabcbaddf")}, 2 expected')
print(f'{Solution().minCut("abaaaaabba")}, 2 expected')
