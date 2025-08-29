from collections import defaultdict
# Mistake 1: Yet another err in indexing: I need to populate my answer out to m+1, n+1, as python is 0-indexed
# This is my first time doing space-optimized 2D DP
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        num_counts = []
        for word in strs:
            one_count = 0
            zero_count = 0
            for character in word:
                if character == "0":
                    zero_count+=1
                elif character == "1":
                    one_count+=1
            num_counts.append((zero_count,one_count))
        
        row = defaultdict(int)
        for zero_count,one_count in num_counts:
            new_row = defaultdict(int)
            for i in range(m+1): #Zeros
                for j in range(n+1): #Ones
                    if j-one_count<0 or i-zero_count<0:
                        new_row[(i,j)] = row[(i,j)]
                    else: 
                        new_row[(i,j)] = max(row[(i,j)],row[(i-zero_count,j-one_count)]+1)
            row = new_row
        return row[(m,n)]
