class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        
        def backtrack(cur,pos,target):
            if target ==0:
                res.append(cur.copy())
                return
            if target <=0:
                return
            #go thrw the every candiates
            prev=-1
            for i in range(pos, len(candidates)):
                #skip duplicates
                if candidates[i]==prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i+1, target-candidates[i])
                cur.pop()
                prev = candidates[i]
        backtrack([],0, target)
        return res
        '''
         Combination Sum Two - Given a collection of positive numbers and a positive target number - Find all unique combinations that sum up to the target - Each number can only be used once - Solutions cannot contain duplicates - Approach: Backtracking (brute force) - Sort the input array - Maintain variables: current combination, index (i), target - Base cases: target equals 0 or target less than 0 (return) - For each candidate, append it to the current combination - Recursively call the function with updated combination, i+1, and target-candidate - Clean up: remove the last candidate from the combination - To eliminate duplicates, check if current candidate equals previous candidate (skip iteration if true) - Initialize previous candidate as -1 - Call the backtracking function with empty combination, index 0, and target from input - Return the result (all combinations) - Solution is efficient with a time complexity of 2^n (n is the size of the input)
        '''
        