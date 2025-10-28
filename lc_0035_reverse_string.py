from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Must be 0(1) memory
        l, r = 0, len(s) - 1
        while l <= r:
            old_left = s[l]
            s[l] = s[r]
            s[r] = old_left
            l += 1
            r -= 1
        print(s)


Solution().reverseString(["h", "e", "l", "l", "o"])
