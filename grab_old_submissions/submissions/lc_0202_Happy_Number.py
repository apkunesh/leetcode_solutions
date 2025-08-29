class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur_num = n
        while True:
            if cur_num in seen:
                return False
            sum_sq = sum([int(char)**2 for char in str(cur_num)])
            if sum_sq == 1:
                return True
            seen.add(cur_num)
            cur_num = sum_sq