class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        index =0

        if needle not in haystack:
            return -1
        else:
            index+= haystack.index(needle)
        return index            