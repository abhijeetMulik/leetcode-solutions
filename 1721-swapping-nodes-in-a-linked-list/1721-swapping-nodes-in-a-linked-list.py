# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = head
        slow = head

        for _ in range(1, k):
            fast = fast.next
        
        prev = fast

        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        prev.val, slow.val = slow.val, prev.val

        return head
        


        