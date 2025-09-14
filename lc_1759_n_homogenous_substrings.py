class Solution:
    def countHomogenous(self, s: str) -> int:
        count, prev, grand_max = 1, s[0], 0
        for i in range(1, len(s)):
            if s[i] == prev:
                count += 1
            else:
                grand_max, prev, count = grand_max + count * (count + 1) // 2, s[i], 1
        grand_max += count * (count + 1) // 2
        return grand_max % (10**9 + 7)
