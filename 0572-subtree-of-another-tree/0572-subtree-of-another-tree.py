# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        def containsSubTree(root):
            if not root:
                return None
            return (
                treesEqual(root,subRoot)
                or containsSubTree(root.left)
                or containsSubTree(root.right)
            )
        def treesEqual(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            return(
                root1.val == root2.val
                and treesEqual(root1.left, root2.left)
                and treesEqual(root1.right, root2.right)
            )
        return containsSubTree(root)
                
            
            
            