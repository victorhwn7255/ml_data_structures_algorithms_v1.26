class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    
    
def deleteNode(node: ListNode):
  next_node = node.next
  node.val = next_node.val
  node.next = next_node.next
  next_node.next = None