class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        count = {}
        l=0 
        
        for r in range(len(s)):
            count[s[r]] = 1+ count.get(s[r],0)
            res = max(res, count[s[r]])
            
            if (r-l+1) - res > k:
                count[s[l]]-=1
                l+=1
        return (r-l+1)
        