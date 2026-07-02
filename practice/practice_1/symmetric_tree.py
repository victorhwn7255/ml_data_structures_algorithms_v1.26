class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

from collections import deque
def isSymmetric(root: TreeNode):
  queue = deque([(root.left, root.right)])
  
  while queue:
    left_node, right_node = queue.popleft()
    
    if left_node is None and right_node is None:
      continue
    
    if left_node is None or right_node is None:
      return False
    
    if left_node.val != right_node.val:
      return False
    
    queue.append((left_node.left, right_node.right))
    queue.append((left_node.right, right_node.left))

  return True
      
    
      