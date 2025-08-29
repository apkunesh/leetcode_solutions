def recurse(digits,i):
    if digits[i] != 9:
        digits[i] += 1
        return digits
    digits[i] = 0
    if i == 0:
        return [1] + digits
    return recurse(digits,i-1)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return recurse(digits,len(digits)-1)