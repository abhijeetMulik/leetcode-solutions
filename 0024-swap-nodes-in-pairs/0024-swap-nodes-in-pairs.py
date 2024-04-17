# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        point = dummy
        while point.next and point.next.next:
            swap1 = point.next
            swap2 = point.next.next

            swap1.next = swap2.next
            swap2.next = swap1

            point.next = swap2
            point = swap1

        return dummy.next
        