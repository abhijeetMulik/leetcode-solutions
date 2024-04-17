# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        for i in range(n - 1):
            fast = fast.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        # print(slow.val)
        slow.next = slow.next.next
        return dummy.next