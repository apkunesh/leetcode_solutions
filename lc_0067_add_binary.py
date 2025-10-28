from collections import deque


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        long, short = (a, b) if len(a) > len(b) else (b, a)
        queue = deque()
        carry = False
        for i in range(len(long)):
            l = long[len(long) - i - 1]
            r = short[len(short) - i - 1] if len(short) - i - 1 >= 0 else "0"
            if l == "0" and r == "0":
                queue.append("0" if carry is False else "1")
                carry = False
            elif (l == "0" and r == "1") or (l == "1" and r == "0"):
                queue.append("1" if carry is False else "0")
                carry = True if (r == "1" and carry) or (l == "1" and carry) else False
            else:
                queue.append("1" if carry else "0")
                carry = True
        if carry:
            queue.append("1")
        queue.reverse()
        return "".join(queue)


soln = Solution().addBinary
print(f"{soln('11','1')} should be 100")
print(f"{soln('1010','1011')} should be 10101")
