from collections import defaultdict

def discover_palindromes(s, l, r, adj):
    if l<0 or r>len(s)-1:
        return # OOB
    if s[l] == s[r]:
        adj[l].add(r+1) # Note that r can be OOB
        discover_palindromes(s,l-1,r+1,adj)

def dfs(s,index,adj,results,list_so_far):
    if index == len(s):
        results.append(list_so_far.copy())
        return
    for child_index in adj[index]:
        list_so_far.append(s[index:child_index])
        dfs(s,child_index,adj,results,list_so_far)
        list_so_far.pop()
    

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        adj = defaultdict(set)
        for i in range(len(s)):
            discover_palindromes(s,i,i,adj)
            discover_palindromes(s,i-1,i,adj)
        results = []
        dfs(s,0,adj,results,[])
        return results