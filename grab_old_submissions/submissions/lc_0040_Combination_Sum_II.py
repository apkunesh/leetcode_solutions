class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Made a conceptual error in deduping: in particular, I needed to not add an element
        # equal to the current target if it had already been added.
        candidates.sort() # nlogn, so the final soln is O(t*n + n*log(n))
        old = [[] for _ in range(target+1)]
        highest_seen = set()
        for i in range(len(candidates)):
            new = [[] for _ in range(target+1)]
            for j in range(target+1):
                new[j] =  old[j].copy() # This is a list of tuple
                if j == candidates[i] and tuple([j]) not in highest_seen:
                    new[j].append(tuple([j]))
                    highest_seen.add(new[j][-1])
                if j-candidates[i]>0:
                    if old[j-candidates[i]]!=[]:
                        for elem in old[j-candidates[i]]:
                            tentative = elem+tuple([candidates[i]])
                            if tentative not in highest_seen:
                                new[j].append(tentative)
                                highest_seen.add(tentative)
            old = new
        return [list(elem) for elem in new[-1]]