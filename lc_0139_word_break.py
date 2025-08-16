# Lots of mistakes around adding the root back in when a word is at its end.

class TreeNode():
    def __init__(self,value:str,is_word:bool=False):
        self.value = value
        self.children={}
        self.is_word = is_word

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TreeNode(value="@")
        for word in wordDict:
            cur_node = root
            for letter in word:
                if cur_node.children.get(letter) is None: # Only spawn if not present
                    cur_node.children[letter] = TreeNode(value=letter)
                cur_node=cur_node.children[letter]
            cur_node.is_word=True
        candidates = set([root])

        for letter in s:

            if not candidates:
                return False
            needs_root = False
            for candidate in candidates:
                if candidate.is_word:
                    needs_root = True
            if needs_root:
                candidates.add(root)
            new_candidates = set()
            for candidate in candidates:
                if letter in candidate.children:
                    new_candidates.add(candidate.children[letter])
            candidates = new_candidates

        if any([elem.is_word for elem in candidates]):
            return True
        return False
