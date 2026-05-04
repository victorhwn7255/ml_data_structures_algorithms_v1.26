class Node:
  def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
    self.val = val
    self.left = left
    self.right = right
    self.next = next

from collections import deque
def connect(root: Node):
  if root is None:
    return None
  
  queue = deque([root])
  
  while queue:
    current_level_size = len(queue)
    for i in range(current_level_size):
      current_node = queue.popleft()
      if i < current_level_size - 1:
        current_node.next = queue[0]
      else:
        current_node.next = None
      if current_node.left:
        queue.append(current_node.left)
      if current_node.right:
        queue.append(current_node.right)
  
  return root