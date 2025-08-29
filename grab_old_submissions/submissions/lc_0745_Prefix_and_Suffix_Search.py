class TrieNode():
    def __init__(self):
        self.children = {}
        self.list_indices = []

class WordTrie():
    def __init__(self,words):
        self.head = TrieNode()
        for i in range(len(words)):
            self.add_word_with_index(words[i],i)
    
    def add_word_with_index(self,word,index):
        cur = self.head
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur.children[letter].list_indices.append(index)
            cur = cur.children[letter]
    
    def find_elements_with_prefix(self,prefix):
        cur = self.head
        for letter in prefix:
            if letter not in cur.children:
                return None
            cur = cur.children[letter]
        return cur.list_indices

class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix_tree = WordTrie(words)
        self.suffix_tree = WordTrie([word[::-1] for word in words])

    def f(self, pref: str, suff: str) -> int:
        prefix_indices = self.prefix_tree.find_elements_with_prefix(pref)
        suffix_indices = self.suffix_tree.find_elements_with_prefix(suff[::-1])
        if prefix_indices is None or suffix_indices is None:
            return -1
        i,j = len(prefix_indices)-1,len(suffix_indices)-1
        while i>=0 and j>=0:
            if prefix_indices[i] == suffix_indices[j]:
                return prefix_indices[i]
            if prefix_indices[i]>suffix_indices[j]:
                i-=1
            else:
                j-=1
        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)