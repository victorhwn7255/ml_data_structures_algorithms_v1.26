class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
def reverseList(head: ListNode):
  if head is None:
    return None
  
  current = head
  prev = None
  
  while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
  
  return prev

