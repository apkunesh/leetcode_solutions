class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        # Naive soln: Simply move along s. For each, scan along. When
        # the # of elements not matching the pattern is <=1, return.
        # This is O(len(s)*len(pattern))
        # It seems poorly-suited to sliding window, since the pattern matches
        # sitewise.
        # Idea: can speed things up a bit by skipping if the ord sum is too different.
        # This is probably not exactly optimal, but saves us a few O(len(pattern)) cycles.
        pattern_ord = 0
        for i in range(len(pattern)):
            pattern_ord += ord(pattern[i])
        L, R = 0, len(pattern) - 1
        if R >= len(s):
            return -1
        substring_ord = 0
        for i in range(len(pattern)):
            substring_ord += ord(s[i])
        while R < len(s):
            if abs(substring_ord - pattern_ord) < 27:
                error_count = 0
                for s_i, p_i in zip(range(L, R + 1), range(len(pattern))):
                    if s[s_i] != pattern[p_i]:
                        error_count += 1
                    if error_count > 1:
                        break
                if error_count < 2:
                    return L
            substring_ord = substring_ord - ord(s[L])
            L += 1
            R += 1
            substring_ord = substring_ord + ord(s[R]) if R < len(s) else 0
        return -1


print(Solution().minStartingIndex("abcdefg", "bcdffg") == 1)
print(Solution().minStartingIndex("ababbababa", "bacaba") == 4)
print(Solution().minStartingIndex("abcd", "dba") == -1)
print(Solution().minStartingIndex("dde", "d") == 0)
