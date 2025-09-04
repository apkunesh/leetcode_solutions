class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n_per_cycle = 2 * (numRows - 1)
        output_str = ""
        for row_ind in range(numRows):
            if row_ind == 0 or row_ind == numRows - 1:
                first_add = n_per_cycle
                second_add = n_per_cycle
            else:
                first_add = n_per_cycle - 2 * row_ind
                second_add = n_per_cycle - first_add
            str_ind = row_ind
            toggle = True
            while str_ind < len(s):
                output_str = output_str + s[str_ind]
                str_ind = str_ind + first_add if toggle else str_ind + second_add
                toggle = not toggle
        return output_str


# print(Solution().convert("PAYPALISHIRING", 3))
