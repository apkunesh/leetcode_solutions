class Solution:
    def smallestNumber(self, n: int) -> int:
        binary_digits = 0
        while n != 0:
            n = n // 2
            binary_digits += 1
        return 2**binary_digits - 1
