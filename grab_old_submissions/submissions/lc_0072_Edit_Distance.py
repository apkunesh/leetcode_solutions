class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #word1 across top, word2 on vertical
        row = list(range(len(word1)+1))
        for i in range(len(word2)):
            new_row = [i+1]
            for j in range(len(word1)):
                if word1[j] == word2[i]:
                    new_row.append(row[j])
                else:
                    add = 1 + row[j+1]
                    swap = 1 + row[j]
                    delete = 1 + new_row[-1]
                    new_row.append(min([add,swap,delete]))
            row = new_row
        return row[-1]
