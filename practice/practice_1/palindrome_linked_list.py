class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    

def isPalindrome(head: ListNode):
  slow = head
  fast = head
  
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  
  prev = None
  if fast:
    current = slow.next
  else:
    current = slow
  
  while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
    
  reversed_half = prev
  
  while reversed_half:
    if reversed_half.val != head.val:
      return False
    reversed_half = reversed_half.next
    head = head.next
  
  return True