class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1
        sign = 1 if x >= 0 else -1
        x = x * sign  # Absolute value
        result = 0
        while x:
            remainder = x % 10
            if result > MAX // 10:
                return 0
            result = result * 10 + remainder
            x = x // 10
        return result * sign
