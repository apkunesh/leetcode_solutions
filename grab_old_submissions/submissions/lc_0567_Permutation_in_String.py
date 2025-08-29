from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding Window problem
        # General idea (not efficient): 
        # Create count of each letter in s1
        # Scan across each len(s1) substring of s2 and modify the dict. If all keys map to 0, we have found a substr.
        # SC: O(len(s1))
        # TC: O(len(s1)*len(s2))
        # More efficient:
        # Slide window, adding and removing from count dependent on l and r pointer
        # At each, assess values in dict. If map to 0, found substr-> return True. Else return False
        # We need only even do the assessment if the right char is in s1
        if len(s2) < len(s1):
            return False
        char_count = defaultdict(int)
        for char in s1:
            char_count[char]+=1
        for i in range(len(s2)):
            left = i-len(s1)
            if left >=0:
                if s2[left] in char_count.keys():
                    char_count[s2[left]]+=1
            if s2[i] in char_count.keys():
                char_count[s2[i]]-=1
                if all(elem == 0 for elem in list(char_count.values())):
                    return True
        # O(len(s2)*len(s1))
        return False
