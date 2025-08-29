
def recurse(string,n,open_count,close_count,string_list):
    if open_count > n:
        return False
    if close_count > open_count:
        return False
    if open_count == n and close_count == n:
        string_list.append(string)
        return True
    recurse(string+'(',n,open_count+1,close_count,string_list)
    recurse(string+')',n,open_count,close_count+1,string_list)
    

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # I'll do this recursively
        result = []
        recurse('',n,0,0,result)
        return result
