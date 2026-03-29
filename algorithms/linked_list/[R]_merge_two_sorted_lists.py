class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
def mergeTwoLists(list1: ListNode, list2: ListNode):
  if list1 is None:
    return list2
  if list2 is None:
    return list1

  head = ListNode(-300)
  current = head
  
  while list1 and list2:
    if list1.val >= list2.val:
      current.next = list2
      list2 = list2.next
    else:
      current.next = list1
      list1 = list1.next
    current = current.next
    
  current.next = list1 if list1 else list2
  
  return head.next