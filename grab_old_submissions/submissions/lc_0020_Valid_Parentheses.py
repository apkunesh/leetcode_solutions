class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = []
        open_to_closed = {'(':')','{':'}','[':']'}
        open_brackets = open_to_closed.keys()
        for i in range(len(s)):
            bracket = s[i]
            if bracket in open_brackets:
                open_stack.append(bracket)
            else:
                if len(open_stack) == 0:
                    return False
                if open_to_closed[open_stack.pop()] != bracket:
                    return False
        return True if not open_stack else False