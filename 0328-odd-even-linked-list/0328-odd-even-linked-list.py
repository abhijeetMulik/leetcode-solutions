# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        prev = head
        curr = head.next
        odd = prev
        even = curr

        while curr and curr.next:
            next_node = curr.next
            prev.next = next_node
            curr.next = next_node.next
            prev = next_node
            curr = next_node.next
        
        prev.next = even

        return odd
        
        