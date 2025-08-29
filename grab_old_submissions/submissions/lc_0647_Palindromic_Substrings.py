class Solution:
    def countSubstrings(self, s: str) -> int:
        row = [True] * len(s)
        palindrome_count = len(s)
        for i in range(1,len(s)):
            new_row = [True] * len(s)
            for j in range(i):
                if s[j] == s[i] and row[j+1] is True:
                    palindrome_count+=1
                else:
                    new_row[j] = False
            row = new_row
        return palindrome_count
