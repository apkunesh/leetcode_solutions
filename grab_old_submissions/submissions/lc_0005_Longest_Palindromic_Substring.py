class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Mistake 1: Silly miss, referencing unbound after tiny refactor
        # Mistake 2: silly miss, didn't actually use the length I found to slice string.
        # Mistake 3: Silly miss, referenced new_row in final return when it wasn't guaranteed to exist.
        # Major error: I basically tried to find a pattern without thinking about the space enough / 
        # what constitutes a real solution. This manifested in failing to properly take into account
        # when a matching letter has already been "used"
        # Reimplemented
        # Mistake 4: forgot to move the new_row to be old_row
        row = [(True,0,"")]*len(s)
        row[0] = (True,1,s[0])
        grand_max = 1
        grand_word = s[0]
        for i in range(1,len(s)):
            new_row = [(True,0,"")] * len(s)
            new_row[i] = (True,1,s[i])
            for j in range(0,i):
                if s[i] == s[j]:
                    if row[j+1][0] is True:
                        total = row[j+1][1]+2
                        new_word = s[i]+row[j+1][2]+s[i]
                        new_row[j] = (True,total,new_word)
                        if total > grand_max:
                            grand_word = new_word
                        grand_max = max(grand_max,total)
                    else:
                        new_row[j] = (False,0,"")
                else:
                    new_row[j] = (False,0,"")
            row = new_row
        return grand_word

                