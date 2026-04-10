class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
def kthSmallest(root: TreeNode, k: int):
  results = []
  
  def inorder(node: TreeNode):
    if node is None:
      return
    
    inorder(node.left)
    results.append(node.val)
    inorder(node.right)
  
  inorder(root)
  return results[k-1]

