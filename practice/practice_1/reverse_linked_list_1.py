class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
def reverseList(head: ListNode):
  if head is None:
    return None
  if head.next is None:
    return head
  
  prev: ListNode = None
  current: ListNode = head
  while current:
    next_node: ListNode = current.next
    current.next = prev
    prev = current
    current = next_node
  
  return prev