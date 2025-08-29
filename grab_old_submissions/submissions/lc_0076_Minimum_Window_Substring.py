# Passed neetcode, TLE'd on Leetcode.
# Attempting again with sliding window approach
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = defaultdict(int)
        for letter in t:
            t_counts[letter]+=1
        L,R=0,0
        s_counts = defaultdict(int)
        
        def check_satisfies(tc,sc): # Note this is an inefficient check -- we can get away with checking only the affected char
            for key,val in tc.items():
                if sc[key] < val:
                    return False
            return True
        
        while check_satisfies(t_counts,s_counts) is False:
            if R == len(s):
                return "" # We reached the end and never satisfied
            if s[R] in t_counts.keys():
                s_counts[s[R]]+=1
            R+=1
        # 0 to R (exclusive) now satisfies the condition
        best_range = [0,R]
        while L<R and R<len(s)+1:
            satisfied = check_satisfies(t_counts,s_counts)
            if satisfied:
                if R-L < best_range[1]-best_range[0]:
                    best_range = [L,R]
                if s[L] in t_counts:
                    s_counts[s[L]]-=1
                L+=1
            else:
                if R == len(s):
                    break
                if s[R] in t_counts:
                    s_counts[s[R]]+=1
                R+=1
        return s[best_range[0]:best_range[1]]