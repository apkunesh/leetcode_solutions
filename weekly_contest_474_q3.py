from time import sleep
from typing import List


class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        """
        New idea: binary search, basically, where the # of hours gives us exactly the number we need.
        """

        def excess_spaces(hours):
            if r[0] == r[1]:
                return hours - hours // r[0] - d[0] - d[1]
            unusable_for_both = (
                hours // (r[0] * r[1]) if r[0] != r[1] else hours // r[0]
            )
            return hours - unusable_for_both - d[0] - d[1]

        left = 0
        right = 10**9 + 1
        mid = (right + left) // 2
        while right >= left:
            sleep(0.1)
            mid = (right + left) // 2
            spaces = excess_spaces(mid)
            print(f"Trying {mid}, got {spaces} spaces excess. RL is {[right,left]}")
            if spaces < 0:
                left = mid + 1
            elif spaces > 0:
                right = mid - 1
            else:
                return mid if excess_spaces(mid - 1) != 0 else mid - 1
        return mid if excess_spaces(mid - 1) != 0 else mid - 1


print(Solution().minimumTime([3, 1], [2, 3]))
# print(Solution().minimumTime([1, 3], [2, 2]))
# print(Solution().minimumTime([2, 1], [3, 4]))
