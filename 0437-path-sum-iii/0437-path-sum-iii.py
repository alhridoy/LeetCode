# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        #prefixSum encountered in the current path
        sums = defaultdict(int)
        sums[0]=1
        #dfs
        def dfs(root, total):
            count = 0
            if root:
                total += root.val
                # Can remove sums[currSum-targetSum] prefixSums to get target
                count = sums[total-targetSum]
                #Add value to prefixSum
                sums[total]+=1
                #Explore children
                count += dfs(root.left,total)+dfs(root.right,total)
                #Remove the path that haven not been explored
                sums[total] -=1
            return count
        return dfs(root,0)
                
                
                	
                
        