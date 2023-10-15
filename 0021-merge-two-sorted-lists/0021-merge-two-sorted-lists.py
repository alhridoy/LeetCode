# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
    
        while list1 and list2:
            if list1.val < list2.val:
                #Link node to list1
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next 
            #update tail pointer
            tail = tail.next
            
            #find non empty list and insert at the last
        if list1:
                tail.next = list1
        elif list2:
                tail.next = list2
        return dummy.next
    '''
    
    Given lists:

list1: 1 -> 3 -> 5 -> None
list2: 2 -> 4 -> None
dummy and node point to a new node with arbitrary value.
list1 value 1 is less than list2 value 2, so link node to list1 and advance list1.
list1 value 3 is greater than list2 value 2, so link node to list2 and advance list2.
list1 value 3 is less than list2 value 4, so link node to list1 and advance list1.
Continue until one list is exhausted. In this case, list2 is shorter.
Link the node to the non-exhausted list (list1 in this case).
Return dummy.next.
Result: 1 -> 2 -> 3 -> 4 -> 5 -> None

Time and Space Complexity:
Time Complexity: O(m + n), where m and n are the lengths of list1 and list2 respectively. This is because in the worst case, we'll traverse both lists fully.

Space Complexity: O(1). This is because we're using a constant amount of space (the dummy node and a couple of pointers) regardless of the input sizes.
    '''
        