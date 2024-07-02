# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = head
        for i in range(k - 1):
            left = left.next
        
        fast = left
        right = head
        while fast and fast.next:
            right = right.next
            fast = fast.next

        tmp = left.val
        left.val = right.val
        right.val = tmp
        return head
        