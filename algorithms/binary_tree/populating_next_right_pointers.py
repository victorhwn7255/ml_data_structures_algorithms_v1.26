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
      node = queue.popleft()
      if i < current_level_size - 1:
        node.next = queue[0]
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)

  return root

