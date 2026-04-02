class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
def addTwoNumbers(l1: ListNode, l2: ListNode):
  dummy_head = ListNode()
  current = dummy_head
  carry = 0
  while l1 or l2 or carry:
    total_sum = carry
    if l1:
      total_sum += l1.val
      l1 = l1.next
    if l2:
      total_sum += l2.val
      l2 = l2.next
    digit = total_sum % 10
    carry = total_sum // 10
    current.next = ListNode(digit)
    current = current.next
  
  return dummy_head.next