class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

from collections import deque
def levelOrder(root: TreeNode):
  if root is None:
    return []
  
  queue = deque([root])
  result = []
  
  while queue:
    level_size = len(queue)
    current_level = []
    for _ in range(level_size):
      current_node = queue.popleft()
      current_level.append(current_node.val)
      if current_node.left:
        queue.append(current_node.left)
      if current_node.right:
        queue.append(current_node.right)
    result.append(current_level)
  
  return result


