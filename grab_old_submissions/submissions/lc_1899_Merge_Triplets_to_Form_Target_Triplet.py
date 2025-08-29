class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        filtered_triplets = []
        found = [False,False,False]
        for triplet in triplets:
            if triplet[0]>target[0] or triplet[1]>target[1] or triplet[2]>target[2]:
                continue # Filter out any which will overwrite (high)
            for i in range(3):
                if triplet[i] == target[i]:
                    found[i] = True
        return True if found==[True,True,True] else False