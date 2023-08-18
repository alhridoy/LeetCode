class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        k = 0

        for i in nums:

            if k < 2 or i!= nums[k-2]:
                nums[k] = i
                k+=1
        return k

'''
Initialization of Placement Index:

Use a pointer k to track the next position in the list where a number should be placed.
Start traversing the list with each number represented by i.
Early List Entries:

For the first two entries of the list (k < 2), always place the numbers without any checks. This ensures that at least two occurrences (if they exist) of the starting numbers are allowed.
Duplication Check:

For subsequent numbers, check if the current number i is the same as the number two positions before the current k. This is done to ensure no number occurs more than twice.
If it's not a third (or further) duplicate, place the number i at the kth position and move the k pointer forward.
Final Result:

Once the entire list is processed, the modified list contains numbers with at most two occurrences in the first k positions. The return value k provides the length of this modified list.
'''

