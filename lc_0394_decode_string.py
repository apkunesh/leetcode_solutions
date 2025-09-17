class Solution:
    def decodeString(self, s: str) -> str:
        digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        number_letter_stack, cur_number = [(1, "")], 0
        for i in range(len(s)):
            if s[i] == "[":
                number_letter_stack.append((cur_number, ""))
                cur_number = 0
            elif s[i] in digits:
                cur_number = cur_number * 10 + int(s[i])
            elif s[i] == "]":
                multiple, subsubstring = number_letter_stack.pop()
                sub_string = multiple * subsubstring
                number_letter_stack[-1] = (
                    number_letter_stack[-1][0],
                    number_letter_stack[-1][1] + sub_string,
                )
            else:  # Just a regular letter
                number_letter_stack[-1] = (
                    number_letter_stack[-1][0],
                    number_letter_stack[-1][1] + s[i],
                )
        return number_letter_stack[0][1]
