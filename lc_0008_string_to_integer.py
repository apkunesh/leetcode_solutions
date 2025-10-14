class Solution:
    def myAtoi(self, s: str) -> int:
        legal_nums = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        neg = False
        pos = 0
        while pos < len(s) and s[pos] == " ":
            pos += 1
        if pos == len(s):
            return 0
        # print(f"whitespace shifted to {pos}")
        if s[pos] in ["+", "-"]:
            if s[pos] == "-":
                neg = True
            pos += 1
        while pos < len(s) and s[pos] == "0":
            pos += 1
        if pos == len(s) or s[pos] not in legal_nums:
            return 0
        result = 0
        while pos < len(s) and s[pos] in legal_nums:
            # print(f"Result val {result} at position {pos}")
            if result == 0:
                result = int(s[pos]) if neg is False else -int(s[pos])
                pos += 1
                continue
            left = result * 10
            to_add = int(s[pos]) if neg is False else -int(s[pos])

            result = left + to_add
            if result > 2**31 - 1:
                result = 2**31 - 1
            elif result < -(2**31):
                result = -(
                    2**31
                )  # Note: if we wante to actually stay inside 2**32, we could decide before we even multiplied.
            pos += 1
        return result


soln = Solution().myAtoi

print(f"{soln('42')} should be 42")
print(f"{soln('   -042')} should be -42")
print(f"{soln('1337c0d3')} should be 1337")
print(f"{soln('0-1')} should be 0")
print(f"{soln('-91283472332')} should be -2147483648")
"-91283472332"
"-91283472332"
"""Input: s = "42"
Output: 42

Input: s = " -042"
Output: -42

Input: s = "1337c0d3"
Output: 1337

Input: s = "0-1"
Output: 0

Input: s = "words and 987"
Output: 0
"""
