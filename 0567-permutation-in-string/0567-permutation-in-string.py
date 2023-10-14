class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        len_s1, len_s2 = len(s1), len(s2)
        
        char_count_s1, char_count_window  = Counter(s1), Counter(s2[:len_s1])
        
        #Lopp remaining characters of s2
        
        for i in range(len_s1, len_s2):
            #Return true if s1 is a permutation of the window
            
            if char_count_s1 == char_count_window:
                return True
            #Move window to next deleting pribous and adding new one
            
            char_count_window[s2[i-len_s1]]-=1
            char_count_window[s2[i]]+=1
            # Return result of comparison between char_count_s1 and char_count_window
        return char_count_s1 == char_count_window
        