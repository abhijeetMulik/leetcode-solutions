# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next
        ans = 0

        while fast.next:
            slow = slow.next
            fast = fast.next.next

        fast = slow.next
        # print(fast.val)

        # reverse the linked list halfway
        prev = None
        curr = head
        while curr != fast:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        head.next = fast
        # print(prev)
        
        while fast:
            ans = max(ans, prev.val + fast.val)
            fast = fast.next
            prev = prev.next

        return ans
        