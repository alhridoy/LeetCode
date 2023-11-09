class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        
        if n ==0:
            return 1
        elif n ==1:
            return x
        elif n== -1:
            return 1/x
        return self.myPow(x, n//2)* self.myPow(x, n//2) * self.myPow(x, n%2)
        
        
        '''
        Divide and Conquer

Take $x^{10}$ and as example

$x^{10} = x^5 * x^5 * x^0$
$x^5 = x^2 * x^2 * x^1$
$x^2 = x^1 * x^1 * x^0$

Complexity
Time complexity: $$O(logN)$$

Space complexity: $$O(logN)$$
        '''
        
        