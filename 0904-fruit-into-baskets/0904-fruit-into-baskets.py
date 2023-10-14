class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = collections.defaultdict(int)
        l,total, res = 0,0,0 
        for r in range(len(fruits)):
            count[fruits[r]]+=1
            total+=1
            while len(count) > 2:
                f = fruits[l]
                count[f]-=1
                total-=1
                l+=1
                #if not window remove it
                if not count[f]:
                    count.pop(f)
            res = max(res, total)
        return res
    
    '''
    - Initialize a hash map to keep track of fruit counts and a variable for the total number of fruits.
- Use a sliding window approach with two pointers (left and right) to traverse the array.
- Increment the count of the current fruit and total when encountering a fruit.
- Ensure the window remains valid (at most two distinct fruit types) by popping from the left if needed.
- Update the result with the maximum total fruit count encountered during traversal.
- Return the result as the length of the longest valid subarray.
    '''
                    
            
        