# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        slow=head
        fast =head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow=slow.next

        head2=slow.next
        slow.next=None

        prev, curr = None, head2

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head2=prev
        
        curr1=head
        curr2=head2

        while curr1 is not None and curr2 is not None:
            next1=curr1.next
            next2=curr2.next

            curr1.next=curr2
            curr2.next=next1

            curr1=next1
            curr2=next2

