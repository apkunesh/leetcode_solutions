from collections import defaultdict


class Solution:
    def longestBalanced(self, s: str) -> int:
        # Idea: for each of the 26 letters, keep track of the count. Then at each start, end, we have constant-time check for whether they're all equal size (?) -- 25 comparisons. Then we expand our radius.
        # O(n**2), but not horrible for 1000 items...
        if len(s) in [1, 2]:
            return len(s)
        grand_result = 2
        for win_len in range(2, len(s) + 1):
            # print(f"TRYING LEN {win_len}")
            letter_count = defaultdict(int)
            for i in range(win_len):
                letter_count[s[i]] += 1
            old_value = None
            match = True
            # print(f"FIRST CHECK {letter_count} with win_len {win_len}")
            for value in letter_count.values():
                if old_value is None:
                    old_value = value
                    continue
                if old_value != value:
                    match = False
                    break
            if match:
                grand_result = win_len
                continue
            for right in range(win_len, len(s)):
                # print(f"USING RIGHT {right}")
                letter_count[s[right - win_len]] -= 1
                letter_count[s[right]] += 1
                old_value = None
                match = True
                # print(f"{letter_count} with val {old_value}")
                for value in letter_count.values():
                    if value == 0:
                        continue
                    if old_value is None:
                        old_value = value
                        # print(f"VALUE SET as {old_value}")
                        continue
                    if old_value != value:
                        match = False
                        break
                if match:
                    # print(f"SET RESULT WITH {right}")
                    grand_result = win_len
                    break
        return grand_result
