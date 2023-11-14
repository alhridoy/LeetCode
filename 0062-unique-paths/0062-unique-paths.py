class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        numPaths = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(0, m):
            for j in range(0,n):
                #base case
                if i==j==0:
                    numPaths[i][j]=1
                    continue
                if i <0 and j <0:
                    numPaths[i][j] =0
                    continue
                #recursion
                numPaths[i][j]=numPaths[i-1][j]+numPaths[i][j-1]
        return numPaths[m-1][n-1]
    
'''

        Initialize the numPaths matrix:

csharp
Copy code
numPaths = [
  [0, 0, 0],
  [0, 0, 0]
]
Iterate through the grid:

For i = 0 and j = 0:

This is the start position. There is exactly 1 way to be here (by starting here).
numPaths[0][0] = 1
For i = 0 and j = 1:

We can only come from the left cell.
numPaths[0][1] = numPaths[0][0] = 1
For i = 0 and j = 2:

Again, we can only come from the left cell.
numPaths[0][2] = numPaths[0][1] = 1
For i = 1 and j = 0:

We can only come from the cell above.
numPaths[1][0] = numPaths[0][0] = 1
For i = 1 and j = 1:

We can come from the left (1 way) or from above (1 way).
numPaths[1][1] = numPaths[1][0] + numPaths[0][1] = 1 + 1 = 2
For i = 1 and j = 2:

We can come from the left (2 ways) or from above (1 way).
numPaths[1][2] = numPaths[1][1] + numPaths[0][2] = 2 + 1 = 3

 down_moves = m-1
        right_moves = n-1
        total_moves = down_moves+right_moves

        # Of the total number of moves, pick some moves to be down
        return math.comb(total_moves, down_moves)
        
'''
        