from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letter_counts = defaultdict(int)
        for char in s:
            letter_counts[char]+=1
        for char in t:
            letter_counts[char]-=1
        for val in letter_counts.values():
            if val !=0:
                return False
        return True