# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        #initialize queue with root value
        q = collections.deque([root])
        while q:
            
            #until q is not non empty
            rightSide = None
            qLen = len(q)

            #go every elements for this level
            for i in range(len(q)):
                #rmv element from left and add to the right
                node = q.popleft()
                #if node none null
                if node:
                    rightSide = node #rightSide will have the last non-null node of this level.
                    q.append(node.left)
                    q.append(node.right)
            #RS is non null
            if rightSide:
                res.append(rightSide.val)
        return res
        '''
        Approach: We'll use a breadth-first search (BFS) traversal using a queue. As we traverse the tree level by level, the last node in each level will be visible from the right side.

Example:

Consider this tree:

markdown
Copy code
    1
   / \
  2   3
   \   \
    5   4
Step-by-Step Execution:

Initialize res to store the result.
Initialize the queue q with the root of the tree (Node with value 1).
Enter the while loop, as the queue is not empty.
Initialize rightSide as None. This variable will store the last non-null node of each level.
Get the current length of the queue (qLen), which gives us the number of nodes at the current level.
Enter the for loop to iterate over the nodes of the current level.
Dequeue the node from the front of the queue.
If the node is not None, update rightSide to the current node and enqueue its left and right children. By the end of the for loop, rightSide will have the last non-null node of this level.
After the for loop, check if rightSide is not None. If it's not, add its value to res.
Repeat steps 3 to 9 until the queue is empty.
Dry Run:

Initial: res = [], q = [1]
1st iteration of while loop: qLen = 1, After processing node 1, q = [2, 3], rightSide = 3. So, append 3 to res.
2nd iteration of while loop: qLen = 2, After processing nodes 2 and 3, q = [None, 5, None, 4], rightSide = 4. So, append 4 to res.
3rd iteration of while loop: qLen = 4, After processing the next level, q will only have None values and rightSide will remain as None.
Exit while loop as all the next elements in the queue are None.
Final Result: res = [3, 4]

Time Complexity:

We're visiting each node exactly once, so the time complexity is O(n), where n is the number of nodes in the tree.
Space Complexity:

The extra space is mainly taken up by the queue. In the worst case, we could have all the leaf nodes in the queue. Hence, the space complexity can be seen as O(w), where w is the maximum width (or number of nodes in the widest level) of the tree.
        '''