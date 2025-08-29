class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        row = [0]*len(s)
        row[0]=1
        grand_max = 1
        for i in range(1,len(s)):
            new_row = row.copy()
            new_row[i]=1
            for j in range(i-1,-1,-1):
                if s[i] == s[j]:
                    new_row[j] = row[j+1]+2
                    grand_max = max(grand_max,new_row[j])
                else:
                    new_row[j] = max(new_row[j+1],row[j])
            row = new_row
        return grand_max
