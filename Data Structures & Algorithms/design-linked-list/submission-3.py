class ListNode:
        def __init__(self, val):
                self.val=val
                self.next=None

class MyLinkedList:

    def __init__(self):
        self.head=ListNode(0)

    def get(self, index: int) -> int:
        curr=self.head.next
        i=0
        while curr:
            if i==index:
                return curr.val
            curr=curr.next
            i+=1
        return -1
            
    def addAtHead(self, val: int) -> None:
        node=ListNode(val)
        node.next=self.head.next
        self.head.next=node

    def addAtTail(self, val: int) -> None:
        node=ListNode(val)
        curr=self.head
        while curr.next is not None:
            curr=curr.next
        curr.next=node

    def addAtIndex(self, index: int, val: int) -> None:
        node=ListNode(val)
        curr=self.head
        if index <=0:
            node.next=self.head.next
            self.head.next=node
            return
        i=0
        while curr:
            if i== index:
                node.next=curr.next
                curr.next=node
                return
            i+=1
            curr=curr.next


    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return

        curr = self.head
        i = 0

        while curr.next is not None:
            if i == index:
                curr.next = curr.next.next
                return

            curr = curr.next
            i += 1   
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)