from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = 0
        second_largest = 0
        for elem in nums:
            if abs(elem) > largest:
                second_largest = largest
                largest = abs(elem)
        return largest * second_largest * 10**5
