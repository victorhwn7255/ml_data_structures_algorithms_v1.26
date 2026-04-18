class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
def mergeTwoLists(list1: ListNode, list2: ListNode):
  dummy_head = ListNode()
  current = dummy_head
  
  if list1 is None:
    return list2
  if list2 is None:
    return list1
  
  while list1 and list2:
    if list1.val >= list2.val:
      current.next = list2
      list2 = list2.next
    else:
      current.next = list1
      list1 = list1.next
    current = current.next
    
  if list1:
    current.next = list1
  if list2:
    current.next = list2
  
  return dummy_head.next
  