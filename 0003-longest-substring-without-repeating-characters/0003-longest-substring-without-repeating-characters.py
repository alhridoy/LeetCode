class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()
        l =0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res

'''
Initialize a character set to keep track of characters in the current window.
Use two pointers, left and right, to define the sliding window.
Iterate through the string with the right pointer.
If the character at the right pointer is a duplicate (already in the character set):
Remove the character at the left pointer from the character set.
Increment the left pointer to slide the window.
Update the result if the current window size is larger than the previous result.
Return the maximum result after iterating through the entire string.

'''