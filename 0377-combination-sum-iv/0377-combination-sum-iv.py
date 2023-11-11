class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        numWays = [1]*(target+1)
        
        for i in range(1,target+1):
            numWays[i] = sum(numWays[i-num] for num in nums if i-num >=0)
        return numWays[target]
        '''
        Initialization:
numWays = [1] * (4 + 1)
This results in numWays = [1, 1, 1, 1, 1].
numWays[0] = 1 signifies that there is 1 way to make the sum 0 (by choosing nothing).
Populating the numWays Array:
We iterate over each i from 1 to target (4 in this case).
For i = 1:
We evaluate sum(numWays[1-num] for num in [1, 2, 3] if 1-num >= 0).
For num = 1, 1 - 1 = 0, so numWays[0] = 1.
For num = 2 and num = 3, 1 - num < 0, so they don't contribute.
The total is 1, so numWays[1] = 1.
For i = 2:
We evaluate the sum for num = 1, 2, and 3 again.
For num = 1, numWays[1] = 1.
For num = 2, numWays[0] = 1.
For num = 3, 2 - 3 < 0, so it doesn't contribute.
The total is 1 + 1 = 2, so numWays[2] = 2.
For i = 3:
Similarly, we find that numWays[3] = 4 (1 way with three 1s, 1 way with one 1 and one 2, 1 way with one 3, 1 way with three 1s and one 2).
For i = 4:
We calculate numWays[4] in a similar manner.
It turns out to be 7, which represents the number of ways to make up 4 using 1, 2, and 3.
Final Result:
numWays[4] = 7
The function returns 7, indicating that there are 7 ways to make the sum 4 using the numbers 1, 2, and 3.

Time Complexity 

O(n⋅target). We do 
n=len(nums) checks every time we compute numWays[i], and we compute numWays[i] 

target times.

Space Complexity 

)
O(target)
        '''