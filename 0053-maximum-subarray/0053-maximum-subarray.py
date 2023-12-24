class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        currentSubArray = maxSubArray = nums[0]
        
        
        
        for num in nums[1:]:
            
            currentSubArray = max( num, num+ currentSubArray)
            
            maxSubArray= max(maxSubArray, currentSubArray)
        return maxSubArray
        