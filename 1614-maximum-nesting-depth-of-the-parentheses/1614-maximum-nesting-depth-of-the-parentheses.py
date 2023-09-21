class Solution:
    def maxDepth(self, s: str) -> int:
                
        depth = 0
        mx =0
        
        for i in s:
            if i =='(':
                depth+=1
                mx= max(depth,mx)
            elif i ==')':
                    depth-=1
        return mx
    '''
    The algorithm tracks the depth of nested parentheses in the string using two counters. It moves through the string character by character, increasing the depth for every opening parenthesis and decreasing for every closing one, updating the maximum depth encountered throughout this traversal.
    '''
        