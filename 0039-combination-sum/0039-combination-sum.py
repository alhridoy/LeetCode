class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        '''
        1. res
        
        backtrack
        
        basecase
        '''
        res = []
        def dfs(i,cur,total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            
            dfs(i, cur, candidates[i]+total)
            
            cur.pop()
            
            
            dfs(i+1, cur, total)
            
        dfs(0, [],0)
        return res
        
        
        '''
        where the goal is to find unique combinations of candidates that sum up to a target value. The video explains the approach of using a backtracking algorithm to solve the problem. It demonstrates how to create a decision tree to explore all possible combinations, making two decisions at each step: whether to include or exclude a candidate. The video also explains the base cases for stopping the recursion and provides the code implementation for the algorithm.
        '''
        