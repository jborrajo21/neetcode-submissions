class Node:
    def __init__(self, key=0, val=0, left=None, right=None):
        self.val = val
        self.key = key
        self.next = left
        self.prev = right

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.nodes = {}
        

    def get(self, key: int) -> int:
        if key in self.nodes:
            node = self.nodes[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            node = Node(key, value)
            if len(self.nodes) == self.capacity:
                self.remove(self.head.next)
            self.add(node)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.nodes[node.key]
    
    def add(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        self.nodes[node.key] = node
        
