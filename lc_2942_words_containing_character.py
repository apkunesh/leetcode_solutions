from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        results = []
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] == x:
                    results.append(i)
                    break
        return results


print(Solution().findWordsContaining(["leet", "code"], "e") == [0, 1])
print(Solution().findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "a") == [0, 2])
print(Solution().findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "z") == [])
