class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Mistake 1: Initializing the first row, I did a mixture of preallocation
        # and appending which ended up breaking the result
        # Error 1: Did not consider the case where s1, s2 do not have enough chars to add to s3
        # s1 across top, s2 on vertical
        # Error 2: did not update indices to reflect the correct from Mistake 1.
        # Error 3: did not consider the case where both match. Real, conceptual mistake here
        # Probably would've been simpler to solve without mistake 1

        # Takeaways: decide solidly on whether to preallocate (seems smarter and more explicit)
        # or to append.
        if len(s1)+len(s2) != len(s3):
            return False
        row = [True]
        for i in range(len(s1)):
            if s3[i] == s1[i]:
                row.append(row[-1])
            else:
                row.append(False)
        print(row)
        for i in range(1,len(s2)+1):
            new_row = [row[0] if s3[i-1]==s2[i-1] else False]
            for j in range(1,len(s1)+1):
                s3_index = i+j-1
                new_row.append(False)
                # First case: s3 at index is the same as s2, then same as val from row above
                if s3[s3_index] == s2[i-1]:
                    print(s3[s3_index] + ' and '+ s2[i-1] + ' match at '  +str([i,j]))
                    new_row[-1] = row[j] or new_row[-1]
                # Second case: s3 at index gives same as s1, then same as vall from left
                if s3[s3_index] == s1[j-1]:
                    print(s3[s3_index] + ' and '+ s1[j-1] + ' match at '  +str([i,j]))
                    new_row[-1] = new_row[-2] or new_row[-1]
            row = new_row
            print(row)
        return row[-1]

