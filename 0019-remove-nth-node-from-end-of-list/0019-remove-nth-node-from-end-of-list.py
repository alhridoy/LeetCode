# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #First create dummy Node
        dummy = ListNode(0, head)
        
        #inizilation
        left = dummy
        right = head
        
        #steps to move right 
        
        while n >0 :
            right = right.next
            n-=1
            #left is now 2 steps apart from head since n =2
        while right:
            left = left.next
            right = right.next
        #Now left is the left position of exact position we want to delete this
        
        #delete
        left.next = left.next.next
        return dummy.next
        