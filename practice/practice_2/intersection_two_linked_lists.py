class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    
def getIntersectionNode(headA: ListNode, headB: ListNode):
  
  point_A = headA
  point_B = headB
  
  while point_A is not point_B:
    point_A = headB if point_A is None else point_A.next
    point_B = headA if point_B is None else point_B.next
  
  return point_A

