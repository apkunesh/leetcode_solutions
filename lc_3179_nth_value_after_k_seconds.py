class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        # So there's the obvious "direct construction" method, which I think is k*n*2, which could be up to 10**9.
        # This is, I think, obviously too slow. So what structure can we find?
        """
        Obviously the value at the end of the matrix at t=0 will be 1 and, at t=1, n.
        Think the best we can do is tabulate by taking the sum of the top element and
        the left element. This is n*k.
        """
        old = [1 for _ in range(n)]
        for _ in range(k):
            new = [1]
            for j in range(1, n):
                new.append(new[-1] + old[j])
            old = new.copy()
        return old[-1] % (10**9 + 7)


soln = Solution().valueAfterKSeconds
print(f"{soln(4,5)} should be 56")
print(f"{soln(5,3)} should be 35")
