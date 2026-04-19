class Node:
  def __init__(self, value=0, key=0):
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
    self.tail.next = self.head
    
  def remove(self, node: Node):
    node.prev.next = node.next
    node.next.prev = node.prev
    
  def add_to_front(self, node: Node):
    current_head = self.head.next
    self.head.next = node
    node.next = current_head
    current_head.prev = node
    node.prev = self.head
    
  
  def get(self, key):
    if key in self.hash_map:
      current_node = self.hash_map[key]
      self.remove(current_node)
      self.add_to_front(current_node)
      return current_node.value
    else:
      return -1
    
    
  def put(self, key, value):
    node = Node(key=key, value=value)
    
    if key in self.hash_map:
      current_node = self.hash_map[key]
      self.remove(current_node)
    elif len(self.hash_map) >= self.capacity:
      last_node = self.tail.prev
      self.remove(last_node)
      del self.hash_map[last_node.key]
    self.add_to_front(node)
    self.hash_map[key] = node
    
    