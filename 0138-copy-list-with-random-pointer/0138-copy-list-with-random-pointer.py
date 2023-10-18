"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        '''
       Use a hash map to map original nodes to their copies - Two-pass algorithm: one for cloning nodes, one for setting pointers - In the first pass, create a copy of each node and add it to the hash map - In the second pass, set the next and random pointers using the hash map - Return the head of the copy list from the hash map 
        '''
        oldToCopy = {None:None}
        
        
        cur = head
        #1st Pass copy Nodes
        
        while cur:
            #copy Nodes
            copy = Node(cur.val)
            oldToCopy[cur]= copy
            cur = cur.next
            
        #2nd pass copy next and random pointers
        
        
        
        cur = head
        
        while cur:
            
            copy = oldToCopy[cur] # start with first Node
            
            copy.next = oldToCopy[cur.next]
            
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]
            
        
        
            
            