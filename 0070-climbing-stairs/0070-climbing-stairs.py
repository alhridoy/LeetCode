class Solution:
    def climbStairs(self, n: int) -> int:
        
        def N (n):
            Ns=[1,1]
            #compute N[i] for i =2...,n
            for i in range(2, n+1):
                Ns[0], Ns[1]= Ns[1], Ns[0]+Ns[1]
            return Ns[1]
        return N(n)
        