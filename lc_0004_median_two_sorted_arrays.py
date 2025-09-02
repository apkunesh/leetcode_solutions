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
        while l < r:
            if nums1[l1] > nums2[l2]:
                r = cand - 1
            else:
                l = cand + 1
            cand = l + r // 2
            l1 = cand - 1
            cand_r = total_len // 2 - cand
            l2 = cand_r - 1
        to_left = cand + cand_r
        to_right = total_len - to_left
        if to_left > to_right:  # Odd
            return max([nums1[l1], nums2[l2]])
        if to_left < to_right:  # Odd
            lcand = nums1[l1 + 1] if l1 < len(nums1) - 1 else 2 * 10**32
            rcand = nums2[l2 + 1] if l2 < len(nums2) - 1 else 2 * 10**32
            return min([lcand, rcand])
        # even
        left_part = [nums1[l1], nums2[l2]]
        right_part = [
            nums1[l1 + 1] if l1 < len(nums2) - 1 else 2 * 10**32,
            nums2[l2 + 1] if l2 < len(nums2) - 1 else 2 * 10**32,
        ]
        left_part.sort()
        right_part.sort()
        return (left_part[1] + right_part[0]) / 2
