from math import log


class Solution:
    def getSum(self, a: int, b: int) -> int:
        return int(log(2**a * 2**b, 2))
