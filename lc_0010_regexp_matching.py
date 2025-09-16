class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        tuple_to_result = {}

        def recurse(i_s, i_p):
            if (i_s, i_p) in tuple_to_result:
                return tuple_to_result[(i_s, i_p)]
            if i_s == len(s) and i_p == len(p):
                # both at the end same time!
                tuple_to_result[(i_s, i_p)] = True
                return tuple_to_result[(i_s, i_p)]
            if i_p == len(p):
                # Finished pattern with leftover letters in string
                tuple_to_result[(i_s, i_p)] = False
                return tuple_to_result[(i_s, i_p)]
            if i_s == len(s):
                # Finished string with some elements left in pattern
                if (len(p) - i_p) % 2 != 0:
                    tuple_to_result[(i_s, i_p)] = False
                    return tuple_to_result[(i_s, i_p)]
                star_loc = i_p + 1
                while star_loc < len(p):
                    if p[star_loc] != "*":
                        tuple_to_result[(i_s, i_p)] = False
                        return tuple_to_result[(i_s, i_p)]
                    star_loc += 2
                tuple_to_result[(i_s, i_p)] = True
                return tuple_to_result[(i_s, i_p)]
            # Check for star case first
            if i_p + 1 < len(p) and p[i_p + 1] == "*":
                zeroth = recurse(i_s, i_p + 2)
                if zeroth == True:
                    tuple_to_result[(i_s, i_p)] = True
                    return tuple_to_result[(i_s, i_p)]
                s_to_match = i_s
                while s_to_match < len(s) and (
                    s[s_to_match] == p[i_p] or p[i_p] == "."
                ):
                    s_to_match += 1
                    result = recurse(s_to_match, i_p + 2)
                    if result == True:
                        tuple_to_result[(i_s, i_p)] = True
                        return tuple_to_result[(i_s, i_p)]
                tuple_to_result[(i_s, i_p)] = False
                return tuple_to_result[(i_s, i_p)]
            # Check for . case
            if p[i_p] == "." or p[i_p] == s[i_s]:
                tuple_to_result[(i_s, i_p)] = recurse(i_s + 1, i_p + 1)
                return tuple_to_result[(i_s, i_p)]
            tuple_to_result[(i_s, i_p)] = False
            return tuple_to_result[(i_s, i_p)]

        return recurse(0, 0)


print(Solution().isMatch("aa", "a") is False)
print(Solution().isMatch("nnn", "n*") is True)
print(Solution().isMatch("xyz", ".*z") is True)
print(Solution().isMatch("a", "ab*") is True)
