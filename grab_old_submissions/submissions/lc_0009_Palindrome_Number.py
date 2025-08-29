from math import log10, floor
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        reverse = 0
        x_copy = x
        while x > 0:
            rem = x%10
            reverse = reverse*10+rem
            x = (x-rem)/10
        return reverse == x_copy