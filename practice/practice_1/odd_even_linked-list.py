class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
def oddEvenList(head: ListNode):
  if head is None or head.next is None:
    return head
  
  odd_node = head
  even_node = head.next
  even_head = even_node

  while even_node and even_node.next:
    odd_node.next = even_node.next
    odd_node = odd_node.next
      
    even_node.next = odd_node.next
    even_node = even_node.next
  
  odd_node.next = even_head
  
  return head