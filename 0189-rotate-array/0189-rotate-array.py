class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = len(nums)
        if L == k: return
        k = k%L 
        nums.reverse()
        for i in range(k//2):
            nums[i], nums[k-1-i]= nums[k-1-i],  nums[i]
        for i in range(k, (L+k)//2):

            nums[i], nums[L-1-i+k] = nums[L-1-i+k], nums[i]

    '''

    Initialization: Given a list nums and an integer k, our goal is to rotate the list k positions to the right.
Pre-processing:
Find the actual rotation needed by computing k = k % len(nums). This handles cases where k is greater than the length of nums.
Reverse the entire list. This step prepares the list for subsequent operations.
First Half Swap:
Rotate the first k elements in place. This is achieved by swapping elements symmetrically around the middle of the first k elements.
Second Half Swap:
Start from the kth position, rotate the remaining elements of the list by swapping elements symmetrically until the midpoint of the list.
Outcome: The combination of the reversed list and the two subsequent swaps rotates the list by k positions to the right.
'''
        