class Node:
  def  __init__(self, key=0, value=0):
    self.value = value
    self.key = key
    self.next = None
    self.prev = None

class LRUCache:
  def __init__(self, capacity: int):
    self.hash_map = {}
    self.capacity = capacity
    self.head = Node()
    self.tail = Node()
    self.head.next = self.tail
    self.tail.prev = self.head
  
  def remove(self, node:Node):
    node.next.prev = node.prev
    node.prev.next = node.next
  
  def add_to_front(self, node:Node):
    current_head = self.head.next
    self.head.next = node
    node.prev = self.head
    node.next = current_head
    current_head.prev = node
  
  def get(self, key: int) -> int:
    if key in self.hash_map:
      current_node = self.hash_map[key]
      self.remove(current_node)
      self.add_to_front(current_node)
      return current_node.value
    else:
      return -1
    
  def put(self, key: int, value: int) -> None:
    node = Node(key=key, value=value)
    if key in self.hash_map:
      current_node = self.hash_map[key]
      self.remove(current_node)
    elif len(self.hash_map) >= self.capacity:
      current_node = self.tail.prev
      self.remove(current_node)
      del self.hash_map[current_node.key]
    self.add_to_front(node)
    self.hash_map[key] = node