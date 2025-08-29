class Solution:
    # Mistake 1: didn't think to append this element :ghost:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.recurse(1,[],result,k,n)
        return result

    def recurse(self,elem,cur_set,result,k,n):
        if len(cur_set) == k:
            result.append(cur_set.copy())
            return
        elif elem > n:
            return
        for i in range(elem,n+1): # Need to actually get to n -- 1-indexed.
            cur_set.append(i)
            self.recurse(i+1,cur_set,result,k,n)
            cur_set.pop()