from collections import defaultdict


class Solution:
    def longestBalanced(self, s: str) -> int:
        # Since we have only 3 elements, we should look for places where:
        # 1) We have N repeats of the same element
        # 2) We have exactly half of one element and half of another, divisible by 2
        # 3) We have exactly 1/3 1/3 1/3 of all 3 elements, divisible by 3.
        # We can count the # of elements for each of i, j, k up to index i. This is O(n).
        # Then we can check for each of the 3 conditions above and see where the longest lives.
        if len(s) < 3:
            return len(s)
        grand_result = 2
        as_count = [1 if s[0] == "a" else 0]
        bs_count = [1 if s[0] == "b" else 0]
        cs_count = [1 if s[0] == "c" else 0]
        for i in range(1, len(s)):
            as_count.append(as_count[-1])
            bs_count.append(bs_count[-1])
            cs_count.append(cs_count[-1])
            if s[i] == "a":
                as_count[-1] += 1
            elif s[i] == "b":
                bs_count[-1] += 1
            else:
                cs_count[-1] += 1
        for window_size in range(len(s), 1, -1):
            for start in range(0, len(s) - window_size):
                i, j = start, start + window_size
                left_a = as_count[i - 1] if i - 1 > -1 else 0
                left_b = bs_count[i - 1] if i - 1 > -1 else 0
                left_c = cs_count[i - 1] if i - 1 > -1 else 0
                local_ac = as_count[j] - left_a
                local_bc = bs_count[j] - left_b
                local_cc = cs_count[j] - left_c
                if (j - i + 1) % 3 == 0:
                    if local_ac == local_bc and local_cc == local_bc:
                        return j - i + 1
                if (j - i + 1) % 2 == 0:
                    if (
                        (local_ac == 0 and local_bc == local_cc)
                        or (local_bc == 0 and local_ac == local_cc)
                        or (local_cc == 0 and local_bc == local_ac)
                    ):
                        return j - i + 1
                if (
                    (local_ac == j - i + 1)
                    or (local_bc == j - i + 1)
                    or (local_cc == j - i + 1)
                ):
                    return j - i + 1
        return 2
