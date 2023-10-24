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
        