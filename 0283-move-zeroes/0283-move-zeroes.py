class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0

        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r]= nums[r], nums[l]
                l+=1
        return nums

        '''
Consider the list nums = [0, 2, 0, 3, 4, 0, 5].

Initially: l = 0, r = 0 (nums[0] = 0). Since nums[0] is zero, no swap occurs.

Next iteration: l = 0, r = 1 (nums[1] = 2). Since nums[1] is non-zero, we swap nums[l] and nums[r] (effectively, this doesn't change anything in this particular instance). Increment l.

Next iteration: l = 1, r = 2 (nums[2] = 0). No swap as nums[2] is zero.

Continuing this process, whenever a non-zero value is found, it is placed at the next available spot as indicated by l.

The final modified list becomes: [2, 3, 4, 5, 0, 0, 0].


        '''
