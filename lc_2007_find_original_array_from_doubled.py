from collections import defaultdict
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        elem_count = defaultdict(int)
        for elem in changed:
            elem_count[elem] += 1
        result = []
        sorted_elements = list(elem_count.keys())
        sorted_elements.sort(reverse=True)  # Now arranged from high to low
        for element in sorted_elements:
            large, small = element, element / 2
            while elem_count[large] > 0:
                elem_count[large] -= 1
                if elem_count[small] > 0:
                    result.append(int(small))
                    elem_count[small] -= 1
                else:
                    return []
        return result


soln = Solution().findOriginalArray

print(f"{soln([1,3,4,2,6,8])} should be [1,3,4]")
print(f"{soln([6,3,0,1])} should be []")
