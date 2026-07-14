class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
def buildTree(preorder: list[int], inorder: list[int]):
  inorder_index = {}
  for index, value in enumerate(inorder):
    inorder_index[value] = index
    
  preorder_index = 0
  
  def dfs(left_index, right_index):
    if left_index > right_index:
      return None
    
    nonlocal preorder_index
    root = TreeNode(val=preorder[preorder_index])
    preorder_index += 1
    
    middle_index = inorder_index[root.val]
    root.left = dfs(left_index, middle_index - 1)
    root.right = dfs(middle_index + 1, right_index)
    
    return root
  
  return dfs(0, len(preorder)-1)