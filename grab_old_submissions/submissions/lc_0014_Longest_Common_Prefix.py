class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        result = ""
        min_len = min([len(elem) for elem in strs])
        for j in range(min_len):
            cur_char = strs[0][j]
            for i in range(1,len(strs)):
                if cur_char != strs[i][j]:
                    return result
            result = result + cur_char
        return result