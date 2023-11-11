class Solution:
    def numDecodings(self, s: str) -> int:
        
        nums = {str(n) for n in range(1,27)}
        
         # starts with base case: numWays[len(s)+1] = 0, numWays[len(s)] = 1
        numWays = [0]*(len(s)+2)
        # [0, 0, 0, 0, 0] (for len(s) + 2, which is 3 + 2 in this case).
        
        numWays[len(s)] = 1 #, one way to decode an empty string.
        
        
        #backwards
        
        for i in range(len(s)-1,-1,-1):
            numWays[i]= (numWays[i+1] if s [i:i+1] in nums else 0)+(numWays[i+2] if s[i:i+2] in nums else 0)
        return numWays[0]
        
        