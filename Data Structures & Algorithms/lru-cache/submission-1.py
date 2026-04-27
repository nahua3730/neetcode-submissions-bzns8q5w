class Node:
    def __init__(self, key, value):
       self.key=key
       self.value=value
       self.prev=None
       self.next=None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.right=Node(0,0)
        self.left=Node(0,0)
        self.right.prev=self.left
        self.left.next=self.right
    def remove(self, node):
        prev_node=node.prev
        next_node=node.next
        prev_node.next=next_node
        next_node.prev=prev_node

    def insert(self,node):
        prev_node=self.right.prev
        next_node=self.right
        prev_node.next=node
        node.prev=prev_node
        node.next=next_node
        next_node.prev=node
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node=self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        