class Node:
  def __init__(self, key=0, val=0):
    self.key = key
    self.val = val
    self.next = None
    self.prev = None
    
class LRUCache:
  def __init__(self, capacity: int):
    self.cache = {}
    self.capacity = capacity
    self.head = Node()
    self.tail = Node()
    self.head.next = self.tail
    self.tail.prev = self.head
  
  def remove(self, node:Node):
    node.prev.next = node.next
    node.next.prev = node.prev
    
  def add_to_front(self, node: Node):
    temp = self.head.next
    self.head.next = node
    temp.prev = node
    node.prev = self.head
    node.next = temp
  
  def get(self, key: int) -> int:
    if key in self.cache:
      node = self.cache[key]
      self.remove(node)
      self.add_to_front(node)
      return node.val
    else:
      return -1
    
  def put(self, key: int, value: int) -> None:
    node = Node(key, value)
    if key in self.cache:
      current_node = self.cache[key]
      self.remove(current_node)
    elif len(self.cache) >= self.capacity:
      current_node = self.tail.prev
      self.remove(current_node)
      del self.cache[current_node.key]
    
    self.add_to_front(node)
    self.cache[key] = node
    