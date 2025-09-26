from collections import Counter


class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        # Two forms of palindrome:
        # - single chars
        # - a*a where * is 0 or more palindromes.
        n_uniques_cache = {}
        for length in range(1, len(s)):
            letter_counter = Counter(s[0 : length + 1])
            uniques = set(s[0 : length + 1])
            n_uniques_cache[(0, length)] = len(uniques)
            for start in range(1, len(s) - length + 1):
                end = start + length
                letter_counter[s[start - 1]] -= 1
                if letter_counter[s[start - 1]] == 0:
                    uniques.remove(s[start - 1])
                letter_counter[s[end]] += 1
                if letter_counter[s[end]] == 1:
                    uniques.add(s[end])
                n_uniques_cache[(start, end)] = len(uniques)

        cache = {
            (i, i): 1 for i in range(len(s))
        }  # Each single char forms a palindrome

        _ = s
        return 0 % 10**9 + 7


print(Solution().countPalindromicSubsequences("bccb") == 6)
print(
    Solution().countPalindromicSubsequences(
        "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"
    )
    == 104860361
)
