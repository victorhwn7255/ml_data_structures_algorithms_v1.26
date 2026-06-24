class TreeNode:
  def  __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

from collections import deque
 
def zigzagLevelOrder(root: TreeNode):
  if root is None:
    return []
  
  results = []
  queue = deque([root])
  left_to_right = 1
  
  while queue:
    level_size = len(queue)
    level = deque([])
    for _ in range(level_size):
      node = queue.popleft()
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
      if left_to_right % 2 == 1:
        level.append(node.val)
      if left_to_right % 2 == 0:
        level.appendleft(node.val)

    results.append(list(level))
    left_to_right += 1

  return results