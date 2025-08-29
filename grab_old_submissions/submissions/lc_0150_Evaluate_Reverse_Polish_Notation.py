class RPNode():
    def __init__(self,val):
        self.val = val
        self.is_operator = val in ['+','-','*','/']
        self.left = None
        self.right = None

    def evaluate(self):
        if not self.is_operator:
            raise Exception("Cannot be called on nodes which are numeric")
        left = int(self.left.val) if not self.left.is_operator else self.left.evaluate()
        right = int(self.right.val) if not self.right.is_operator else self.right.evaluate()
        if self.val == '+':
            return right + left
        elif self.val == '-':
            return right-left
        elif self.val == '*':
            return right * left
        elif self.val == '/':
            return int(right / left)
        else:
            raise Exception("This should not be accessible")

def construct(tokens):
    node = RPNode(tokens.pop())
    if not node.is_operator:
        return node # Numeric
    node.left = construct(tokens)
    node.right = construct(tokens)
    return node

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Idea: this is a tree, basically. We're creating branches for which leaves are numbers.
        if len(tokens)==1:
            return int(tokens[0])
        head = construct(tokens)
        return head.evaluate()
