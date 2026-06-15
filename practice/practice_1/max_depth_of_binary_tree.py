class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
def maxDepth(root: TreeNode):
  
  def dfs(node: TreeNode):
    if node is None:
      return 0
    return 1 + max(dfs(node.left), dfs(node.right))
  
  return dfs(root)