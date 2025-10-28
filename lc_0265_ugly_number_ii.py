class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglies = [1]
        i2, i3, i5 = 0, 0, 0
        while len(uglies) < n:
            new_ugly = min([2 * uglies[i2], 3 * uglies[i3], 5 * uglies[i5]])
            uglies.append(new_ugly)
            if 2 * uglies[i2] == new_ugly:
                i2 += 1
            if 3 * uglies[i3] == new_ugly:
                i3 += 1
            if 5 * uglies[i5] == new_ugly:
                i5 += 1
        return uglies[-1]


soln = Solution().nthUglyNumber
print(f"{soln(10)} should be 12")
print(f"{soln(1)} should be 1")
