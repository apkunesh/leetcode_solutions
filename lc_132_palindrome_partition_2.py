class Solution:
    def minCut(self, s: str) -> int:
        table, rows, cols = [], len(s), len(s)
        column_zero_map = {}

        def get_last_zero_cand(i, j):
            maybe_zero_row = column_zero_map.get(j)
            if maybe_zero_row is None:
                return 3000

            ref_row = i - maybe_zero_row - 1
            ref_col = j + maybe_zero_row + 1
            if ref_row < 0 or ref_row >= rows or ref_col < 0 or ref_row >= cols:
                return 3000
            return min(
                table[ref_row][ref_col] + 1,
                get_last_zero_cand(ref_row, ref_col),
            )

        for _ in range(rows):
            local_row = []
            for j in range(cols):
                local_row.append(None)
            table.append(local_row)
        for j in range(cols):
            table[0][j] = 0
        for i in range(1, rows):
            for j in range(cols - i):
                compare_ind = i + j
                # we have a match
                if s[j] == s[compare_ind]:
                    # print("Match found between ", [j, compare_ind])
                    # print("Chars: ", [s[j], s[compare_ind]])
                    if compare_ind - j == 1 or table[i - 2][j + 1] == 0:
                        # print("Setting entry to zero: ", [i, j])
                        table[i][j] = 0
                        column_zero_map[j] = i
                        continue
                # no match; compare candidates
                upper_cand = table[i - 1][j] + 1
                up_right_cand = table[i - 1][j + 1] + 1
                last_zero_cand = get_last_zero_cand(i, j)
                table[i][j] = min([upper_cand, up_right_cand, last_zero_cand])
        # for row in table:
        # print(row)
        return table[-1][0]


print(Solution().minCut("aab") == 1)
print(Solution().minCut("a") == 0)
print(Solution().minCut("ab") == 1)
print(Solution().minCut("dabcbaddf") == 2)
print(Solution().minCut("abaaaaabba") == 2)
