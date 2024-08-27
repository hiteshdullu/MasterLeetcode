class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for i in strs:
            w = [0]*26
            for j in i:
                w[ord(j)-ord('a')]+=1
            w = tuple(w)
            if w in m:
                m[w].append(i)
            else:
                m[w] = [i]
        return m.values()
