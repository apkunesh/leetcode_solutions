from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        grand_result = 0
        for i in range(len(words)):
            for j in range(len(pref)):
                if words[i][j] != pref[j]:
                    break
                if j == len(pref) - 1:
                    grand_result += 1
        return grand_result


print(Solution().prefixCount(["pay", "attention", "practice", "attend"], "at") == 2)
print(Solution().prefixCount(["leetcode", "win", "loops", "success"], "code") == 0)
