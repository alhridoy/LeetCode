class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1]* (len(nums))
        prefix = 1
        for i in range( len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res
    '''
    The solution involves computing prefix and postfix products without using extra memory.
To compute prefix products, the presenter starts from the beginning of the input array, storing the cumulative product in each step. This is multiplied by the value at the current position to get the prefix product for that position.
To compute postfix products, the presenter starts from the end of the input array and updates the cumulative product by multiplying it with the value at the current position. This is then multiplied by the value in the result array for the corresponding position.
The final output array contains the results for each element, which are the products of their respective prefix and postfix values.
    '''
        