# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        length = 0
        curr = head
        ans = 0

        while curr.next:
            length += 1
            curr = curr.next
        
        curr = head
        while curr:
            ans += curr.val * (2 ** length)
            length -= 1
            curr = curr.next

        return ans

        

        