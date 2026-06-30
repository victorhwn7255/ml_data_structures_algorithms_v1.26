class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
def isValidBST(root: TreeNode):
  
  def dfs(node: TreeNode, upper_bound, lower_bound):
    if node is None:
      return True
    
    if node.val >= upper_bound or node.val <= lower_bound:
      return False
    
    return (
      dfs(node.left, node.val, lower_bound) 
      and dfs(node.right, upper_bound, node.val)
      )
  
  return dfs(root, float('inf'), float('-inf'))