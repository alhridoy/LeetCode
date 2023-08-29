class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        totalSum = sum(nums)
        leftSum =0

        for i in range(len(nums)):
            rightSum = totalSum - nums[i]-leftSum
            if leftSum == rightSum:
                return i
            leftSum+=nums[i]
        return -1
'''
Initialize variables: total sum, left sum (initially 0).

Iterate through each index in the array.

For each index:

Calculate right sum: total sum - left sum - current element's value.
If left sum equals right sum, return the current index as the pivot index.
Update left sum by adding the current element's value.
If no pivot index is found, return -1.

The algorithm runs in O(n) time due to single pass through the array.

✅ Calculate the total sum of the array.

✅ Maintain a running left sum while iterating.

✅ Calculate right sum using total sum, left sum, and current element's value.

✅ Return the leftmost pivot index found or -1 if none is found.

'''