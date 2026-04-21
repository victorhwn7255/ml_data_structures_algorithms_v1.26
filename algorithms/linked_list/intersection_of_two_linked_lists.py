class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
  

def getIntersectionNode(headA: ListNode, headB: ListNode):
  if headA is None or headB is None:
    return None
  
  point_A = headA
  point_B = headB
  
  while point_A is not point_B:
    if point_A is None:
      point_A = headB
    else:
      point_A = point_A.next
      
    if point_B is None:
      point_B = headA
    else:
      point_B = point_B.next
  
  return point_A

