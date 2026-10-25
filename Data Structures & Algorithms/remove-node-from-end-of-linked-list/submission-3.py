# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp=[]

        curr=head
        while curr:
            tmp.append(curr)
            curr=curr.next
        
        removeIdx=len(tmp)-n

        if removeIdx==0:
            return head.next
        
        tmp[removeIdx-1].next=tmp[removeIdx].next
        return head
        
