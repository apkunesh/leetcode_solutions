class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def recurse(s, p):
            if len(s) == 0 and len(p) == 0:
                # End of both, it worked!
                return True
            if len(s) == 0 or len(p) == 0:
                # Ran out of one before the other was complete -- not full match
                return False
            # Look out for repeats
            if len(p) > 1 and p[1] == "*":
                # Case 1: 0 occurrences
                if recurse(s[0:], p[2:]) is True:
                    return True
                s_ind = 0
                while s_ind < len(s) and (
                    s[s_ind] == p[0] or p[0] == "."
                ):  # This one could get costly
                    # remaining_s = '' if s_ind == len(s)-1 else s[s_]
                    new_match = recurse(s[s_ind + 1 :], p[2:])
                    if new_match:
                        return True
                    s_ind += 1
                return False  # No match found
            # Look out for single wildcards
            if p[0] == ".":
                return recurse(s[1:], p[1:])
            # So it's just a regular letter match
            return False if p[0] != s[0] else recurse(s[1:], p[1:])

        return recurse(s, p)


# s = "aab"
# p = "c*a*b"
# Expect true
s = "ab"
p = ".*c"
# Expect false
print(Solution().isMatch(s, p))
