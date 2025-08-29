from math import floor
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # First we find the row where the value should live
        outer_left=0
        outer_right = len(matrix)-1
        while outer_left <= outer_right:
            outer_middle = floor((outer_right + outer_left)/2)
            middle_min = matrix[outer_middle][0]
            middle_max = matrix[outer_middle][-1]
            if middle_min > target:
                outer_right = outer_middle - 1
            elif middle_max < target:
                outer_left = outer_middle + 1
            else:
                # Found the row containing a neighborhood around target
                break
        
        if outer_left > outer_right:
            return False

        inner_left = 0
        inner_right = len(matrix[outer_middle]) -1
        while inner_left <= inner_right:
            inner_middle = floor((inner_left+inner_right)/2)
            middle_val = matrix[outer_middle][inner_middle]
            if middle_val > target:
                inner_right = inner_middle - 1
            elif middle_val < target:
                inner_left = inner_middle + 1
            else:
                return True
        return False