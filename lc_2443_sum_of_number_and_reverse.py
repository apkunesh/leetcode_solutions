class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        """
        So we can def do this in O(n) time if we just go 1-n and assess whether the one minus the other gives the result. This would sastisfy the constraints.
        Is that all, though?
        I don't see anything obvious, though there are optimizations inside the O(n).
        """
        for i in range(num):
            forward = str(i)
            reverse = [char for char in forward]
            reverse.reverse()
            reverse_int = int("".join(reverse))
            if i + reverse_int == num:
                return True
        return False


soln = Solution().sumOfNumberAndReverse
print(f"{soln(443)} should be True")
print(f"{soln(63)} should be False")
print(f"{soln(181)} should be True")
