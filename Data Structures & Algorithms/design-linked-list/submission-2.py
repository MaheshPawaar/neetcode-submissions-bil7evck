class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head=ListNode(0)
        self.size=0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr=self.head.next
        for _ in range(index):
            curr=curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        node=ListNode(val)
        node.next=self.head.next
        self.head.next=node
        self.size+=1

    def addAtTail(self, val: int) -> None:
        node=ListNode(val)
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=node
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        curr=self.head
        for _ in range(index):
            curr=curr.next
        node=ListNode(val)
        node.next=curr.next
        curr.next=node
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        curr=self.head

        for _ in range(index):
            curr=curr.next
        curr.next=curr.next.next
        self.size-=1