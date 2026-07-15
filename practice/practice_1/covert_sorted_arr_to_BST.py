class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
def sortedArrayToBST(nums: list[int]):
  
  def dfs(arr: list):
    if len(arr) == 0:
      return None
    
    mid = len(arr) // 2
    root = TreeNode(val=arr[mid])
    root.left = dfs(arr[:mid])
    root.right = dfs(arr[mid+1:])

    return root
  
  return dfs(nums)

