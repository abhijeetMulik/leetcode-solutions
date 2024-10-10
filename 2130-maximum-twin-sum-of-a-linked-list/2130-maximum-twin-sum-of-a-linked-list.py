# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr, slow, fast = head, head, head
        ans = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while curr != slow:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # print(slow)
        # print(prev)
        
        while slow:
            ans = max(ans, slow.val + prev.val)
            slow = slow.next
            prev = prev.next
        
        return ans

        