# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return head
        fast = curr = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        while curr:
            if curr.val != prev.val:
                return False
            curr = curr.next
            prev = prev.next
        
        return True
                