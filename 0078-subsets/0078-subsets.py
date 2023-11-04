class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []
        def dfs(i):
            #base case
            if i >= len(nums):
                res.append(subset.copy())
                return
            #include 
            subset.append(nums[i])
            dfs(i+1) 
            #not include
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
    
    '''
     subset is a collection of elements from the array without considering the order. We also need to consider the empty subset. To solve this problem, we can use backtracking. We start with an empty subset and make a decision for each element of the array: whether to include it or not. We repeat this decision for every element and generate all possible subsets. The time complexity of this solution is O(n * 2^n), where n is the size of the input array. This is because we have 2^n possible subsets and each subset can have up to n elements. Here is the backtracking solution in code: - Initialize an empty array to store the subsets. - Define a recursive function that takes the current index as a parameter. - If the index is out of bounds (greater than or equal to the array length), return. - Add the current subset to the result list. - Recursively call the function for the next element (the left decision) by appending the element to the subset. - Recursively call the function for the next element without including the current element (the right decision) by removing the last element from the subset. - Call the recursive function with the initial index (0). - Return the result list. Note: The order of the subsets in the result list doesn't matter
    '''
        