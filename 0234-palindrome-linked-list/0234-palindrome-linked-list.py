# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        curr = head
        while fast and fast.next:
            fast = fast.next.next
            curr = curr.next
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
        