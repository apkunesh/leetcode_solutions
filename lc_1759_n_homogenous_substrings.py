class Solution:
    def countHomogenous(self, s: str) -> int:
        count = 1
        prev = s[0]
        grand_max = 0
        for i in range(1, len(s)):
            if s[i] == prev:
                count += 1
            else:
                grand_max += count * (count + 1) // 2
                prev = s[i]
                count = 1
        grand_max += count * (count + 1) // 2
        return grand_max % (10**9 + 7)
