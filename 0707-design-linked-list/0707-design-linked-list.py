class ListNode:

    def __init__(self, val = 0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        else:
            curr = self.head
            count = 0
            while count < index:
                curr = curr.next
                count += 1
            if curr:
                return curr.val
            else:
                return -1

        

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head
        self.head = node
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            count = 0
            node = ListNode(val)
            while count < self.size - 1:
                curr = curr.next
                count += 1
            curr.next = node
            self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index > 0 and index < self.size:
            node = ListNode(val)
            curr = self.head
            count = 0
            while count < index - 1:
                curr = curr.next
                count += 1
            node.next = curr.next
            curr.next = node
            self.size += 1
        else:
            return
        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.size > 0:
            self.head = self.head.next
            # self.size -= 1
        elif index > 0 and index < self.size:
            curr = self.head
            count = 0
            while count < index - 1:
                curr = curr.next
                count += 1
            curr.next = curr.next.next
            # self.size -= 1
        else:
            return
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)