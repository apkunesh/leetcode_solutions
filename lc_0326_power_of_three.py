class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # SUPER COOL soln.
        # Basically, there's a largest power of 3 less than the max of 2^31, which
        # we can compute by hand. Any number that cleanly divides this number
        # is itself a power of 3.
        if n < 1:
            return False
        max_power_of_three = 1162261467
        return max_power_of_three % n == 0

        """
        # Think this is basically a math problem, but not sure how to implement log otherwise.
        # Attempting to analyze by bits doesn't do much, though obviously if we can convert to base 3 it's trivial.
        while n%3 == 0:
            n = n//3
            if n == 0:
                return True
        return False
        """
