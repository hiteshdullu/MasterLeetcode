class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s2_len < s1_len:
            return False
        s1_freq = [0]*26
        s2_freq = [0]*26

        for i in range(s1_len):
            s1_freq[ord(s1[i])-ord('a')] += 1
            s2_freq[ord(s2[i])-ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1_freq[i] == s2_freq[i]:
                matches+=1
        
        l = 0
        r = s1_len

        while(matches != 26 and r < s2_len):
            index = ord(s2[r])-ord('a')
            s2_freq[index]+=1
            if s2_freq[index] == s1_freq[index]:
                matches+=1
            elif s2_freq[index] - 1 == s1_freq[index]:
                matches-=1
            r+=1
            index = ord(s2[l])-ord('a')
            s2_freq[index]-=1
            if s2_freq[index] == s1_freq[index]:
                matches+=1
            elif s2_freq[index] + 1 == s1_freq[index]:
                matches-=1
            l+=1
        if matches == 26:
            return True
        return False
