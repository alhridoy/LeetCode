# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal):
            
            if not node:
                return 0
            
            #cuu res =1 cz root is always good
            #if cur node is good or not 
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            # formuala = 1+left(num) + right(num)
            res+=dfs(node.left,maxVal)
            res+=dfs(node.right,maxVal)
            return res 
        #call the entire tree
        return dfs(root,root.val)
    
    
    '''
    The problem is about counting the number of "good" nodes in a binary tree, where a good node is defined as a node where there are no nodes with a greater value along its path from the root. The solution is to use a pre-order traversal of the tree, passing the maximum value encountered so far to the left and right child nodes. The base case is when the node is null, in which case 0 is returned. When a non-null node is encountered, the result is set to 1 if the node's value is greater than or equal to the maximum value encountered, otherwise, it is set to 0. The maximum value encountered is updated. The function is recursively called on the left and right child nodes, and the results are added to the total result. Finally, the total result is returned. By calling the dfs function on the root node with the root value as the initial maximum value, the total number of good nodes in the tree is computed. The time complexity is O(n), where n is the number of nodes in the tree, and the space complexity is O(log n), the height of the tree. Increased height could result in greater space complexity up to O(n).
    '''
        