class Node:
  def __init__(self, key=0, val=0):
    self.key = key
    self.value = val
    self.prev = None
    self.next = None

class LRUCache:

  def __init__(self, capacity: int):
    self.capacity = capacity
    self.cache = {}
    
    self.head = Node()
    self.tail = Node()
    self.head.next = self.tail
    self.tail.prev = self.head

  def remove(self, node: Node):
    node.prev.next = node.next
    node.next.prev = node.prev
  
  def add_to_front(self, node: Node):
    node.next = self.head.next
    node.prev = self.head
    self.head.next.prev = node
    self.head.next = node
  
  def get(self, key: int) -> int:
    if key in self.cache:
      node = self.cache[key]
      self.remove(node)
      self.add_to_front(node)
      return node.value
    else:
      return -1

  def put(self, key: int, value: int) -> None:
    node = Node(key, value)
    
    if key in self.cache:
      self.remove(self.cache[key])
      
    elif len(self.cache) >= self.capacity:
      lru_node = self.tail.prev
      self.remove(lru_node)
      del self.cache[lru_node.key]
      
    self.add_to_front(node)
    self.cache[key] = node