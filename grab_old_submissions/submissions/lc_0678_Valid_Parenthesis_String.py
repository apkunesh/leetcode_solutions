class Solution:
    def checkValidString(self, s: str) -> bool:
        low,high = 0,0
        for letter in s:
            high = high+1 if letter in ["(","*"] else high-1
            low = low+1 if letter == "(" else max(low-1,0)
            if high < 0:
                return False
        return low == 0