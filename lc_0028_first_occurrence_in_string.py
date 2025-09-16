class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Slightly better soln -- this one skips beyond letters which aren't present in the needle.
        if len(needle) > len(haystack):
            return -1
        available_letters = set([letter for letter in needle])
        i = 0
        while i < len(haystack) - len(needle) + 1:
            for j in range(len(needle)):
                if needle[j] != haystack[i + j]:
                    if haystack[i + j] not in available_letters:
                        i = i + j - 1
                    break
                if j == len(needle) - 1:
                    return i
            i += 1
        return -1
