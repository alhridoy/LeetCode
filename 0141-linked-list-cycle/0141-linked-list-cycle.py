# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head
        
        while fast and fast.next:
            
            #slow+1
            
            slow = slow.next
            #Fast +2
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False
        