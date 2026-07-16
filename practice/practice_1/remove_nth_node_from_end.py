class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
def removeNthFromEnd(head: ListNode, n: int):
  dummy = ListNode(0, head)
  fast = dummy
  slow = dummy
  
  for _ in range(n+1):
    fast = fast.next
    
  while fast:
    slow = slow.next
    fast = fast.next
    
  temp = slow.next
  slow.next = temp.next
  
  return dummy.next