class Solution:
    def scoreOfString(self, s: str) -> int:
        grand_result = 0
        for l, r in zip(range(len(s) - 1), range(1, len(s))):
            grand_result += abs(ord(s[r]) - ord(s[l]))
        return grand_result


r1 = Solution().scoreOfString("hello")
assert r1 == 13, r1

r2 = Solution().scoreOfString("zaz")
assert r2 == 50, r2
