class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ''
        
        
        for i in range(len(s)):
            for l, r in ((i,i) , (i,i+1)):
                while l >=0 and r < len(s) and s[l]==s[r]:
                    if(r-l+1) > len(res):
                        res = s[l:r+1]
                    l-=1
                    r+=1
        return res
        '''
        Character at index 0 ('b'):

Odd length: l = 0, r = 0. No expansion. Palindrome is "b".
Even length: l = 0, r = 1. No palindrome as 'b' != 'a'.
Character at index 1 ('a'):

Odd length: l = 1, r = 1. Expand to l = 0, r = 2. Palindrome is "aba".
Even length: l = 1, r = 2. No palindrome as 'a' != 'b'.
Character at index 2 ('b'):

Odd length: l = 2, r = 2. Expand to l = 1, r = 3, then to l = 0, r = 4. Palindrome is "bab".
Even length: l = 2, r = 3. No palindrome as 'b' != 'a'.
Character at index 3 ('a'):

Odd length: l = 3, r = 3. Expand to l = 2, r = 4. Palindrome is "aba", but "bab" is longer.
Even length: l = 3, r = 4. No palindrome as 'a' != 'd'.
Character at index 4 ('d'):

Odd length: l = 4, r = 4. No expansion. Palindrome is "d".
Even length: l = 4, r = 5 is out of bounds. No palindrome.

        '''