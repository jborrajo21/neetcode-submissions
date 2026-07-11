class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.nodes = {}
        # Dummies
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head
        self.capacity = capacity
        self.size = 0
        

    def get(self, key: int) -> int:
        node = self.nodes[key] if key in self.nodes.keys() else None
        
        if node:
            self._remove(node)
            self._add_to_tail(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.nodes and self.nodes[key]:
            node = self.nodes[key]
            node.val = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            node = Node(key, value)
            if self.size < self.capacity:
                self.size += 1
            else:
                self._remove(self.head.next)
            self._add_to_tail(node)

    
    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        self.nodes[node.key] = None
    
    def _add_to_tail(self, node: Node) -> None:
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        self.nodes[node.key] = node
