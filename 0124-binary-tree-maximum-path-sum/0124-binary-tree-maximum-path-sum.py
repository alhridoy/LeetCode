# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        def dfs(root):
            
                if not root:
                    return 0
                leftMax = dfs(root.left)
                rightMax = dfs(root.right)
                #update leftMax and rightMax, avoid negative
                leftMax = max(leftMax, 0)
                rightMax = max(rightMax, 0)

                #he maximum path sum that starts in the left subtree, passes through the node, and then goes into the right subtree. 
                res[0] = max(res[0], root.val+leftMax+rightMax)

                #without split, considering parent node and best path contribution from left or right
                return root.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]
        