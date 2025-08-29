class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n_layers = len(matrix)//2
        for i in range(n_layers):
            lower_bound_index = i
            upper_bound_index = len(matrix)-1-i
            for j in range(upper_bound_index - lower_bound_index):
                TL = matrix[lower_bound_index][lower_bound_index+j]
                TR = matrix[lower_bound_index+j][upper_bound_index]
                BR = matrix[upper_bound_index][upper_bound_index-j]
                BL = matrix[upper_bound_index-j][lower_bound_index]
                matrix[lower_bound_index][lower_bound_index+j] = BL
                matrix[lower_bound_index+j][upper_bound_index] = TL
                matrix[upper_bound_index][upper_bound_index-j] = TR
                matrix[upper_bound_index-j][lower_bound_index] = BR

