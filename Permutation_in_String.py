class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        if s2_len < s1_len:
            return False
        
        s1_wc = [0]*26
        s2_wc = [0]*26

        for i in s1:
            s1_wc[ord(i)-ord('a')]+=1
        
        for i in range(s1_len):
            s2_wc[ord(s2[i])-ord('a')]+=1

        l = 0
        r = s1_len
        while r < s2_len:
            if s1_wc == s2_wc:
                return True
            s2_wc[ord(s2[l])-ord('a')]-=1
            s2_wc[ord(s2[r])-ord('a')]+=1
            l+=1
            r+=1
        if s1_wc == s2_wc:
                return True
        return False
