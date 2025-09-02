from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        if len(nums2) < len(nums1):
            dummy = nums1.copy()
            nums1 = nums2.copy()
            nums2 = dummy
        l, r = 0, len(nums1)
        cand = l + r // 2 + 1
        l1 = cand - 1  # Can be -1; in this case, not included at all.
        cand_r = total_len // 2 - cand
        l2 = cand_r - 1
        is_even = total_len % 2 == 0
        while l < r:
            if nums1[l1] > nums2[l2]:
                r = cand - 1
            else:
                l = cand + 1
            cand = l + r // 2
            l1 = cand - 1
            cand_r = total_len // 2 - cand
            l2 = cand_r - 1
        left_results = (
            [nums1[l1], nums1[l1 + 1]] if l1 < len(nums1) - 1 else [nums1[l1]]
        )
        right_results = (
            [nums2[l2], nums2[l2 + 1]] if l2 < len(nums2) - 1 else [nums2[l2]]
        )
        all = left_results + right_results
        all.sort()
        if is_even:
            return all[1] + all[2] // 2
        else:
            return all[2]
