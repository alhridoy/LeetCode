class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l +r ) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l = mid+1
            else:
                r = mid -1
        return l

        '''
        Consider the list nums = [1, 3, 5, 6] and target = 4.

Initially: l = 0, r = 3, mid = 1 (nums[1] = 3)

target (4) > nums[mid (1)] (3): So, we move to the right half: l becomes mid + 1 = 2.

Next iteration: l = 2, r = 3, mid = 2 (nums[2] = 5)

target (4) < nums[mid (2)] (5): Move to the left half: r becomes mid - 1 = 1.

Now, l > r, so we exit the loop. At this point, l = 2 which indicates the position where 4 should be inserted (between 3 and 5). Thus, the function returns 2.


        '''