# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        leftprev = dummy

        for _ in range(1, left):
            leftprev = leftprev.next
            curr = curr.next
        
        prev = None
        for _ in range(left, right + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        leftprev.next.next = curr
        leftprev.next = prev

        return dummy.next