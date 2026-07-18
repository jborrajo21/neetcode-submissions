class Node:
    def __init__(self, key='', val=False):
        self.key = key
        self.val = val
        self.children = [None] * 26

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not node.children[idx]:
                node.children[idx] = Node(char)
            node = node.children[idx]
        node.val = True


    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return node.val

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            idx = ord(char) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return True