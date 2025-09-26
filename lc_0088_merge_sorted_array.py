from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Idea: move everything to the end of nums1 (O(n)). Then simply merge sort in the typical way.
        _ = n
        end_ind = len(nums1) - 1
        for ind in range(m - 1, -1, -1):
            nums1[end_ind] = nums1[ind]
            end_ind -= 1
        print("After move ", nums1)
        # Great, now the first element is ad end_ind+1
        p1 = end_ind + 1
        p2 = 0
        p_res = 0
        # And we can merge based on magnitude
        while p_res < len(nums1):
            cand1 = nums1[p1] if p1 < len(nums1) else 10**10
            cand2 = nums2[p2] if p2 < len(nums2) else 10**10
            if cand1 < cand2:
                nums1[p_res] = cand1
                p1 += 1
            else:
                nums1[p_res] = cand2
                p2 += 1
            p_res += 1
        print(nums1)


print(Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(Solution().merge([1], 1, [], 0))
print(Solution().merge([0], 0, [1], 1))
