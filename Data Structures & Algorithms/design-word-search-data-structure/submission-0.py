class Node:
    def __init__(self, val=False):
        self.val = val
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.val = True
        

    def search(self, word: str) -> bool:
        return self._search(self.root, word)

    def _search(self, root, word):
        if not word: return root.val
        char = word[0]
        if char == '.':
            for key in root.children:
                if self._search(root.children[key], word[1:]):
                    return True
        elif char in root.children:
            return self._search(root.children[char], word[1:])
        return False
        