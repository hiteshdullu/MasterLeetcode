class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        n = len(words)
        dp = [0]*(n+1)
        for i in range(n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                dp[i+1] = dp[i]+1
            else:
                dp[i+1] = dp[i]
        ans = []
        for i in range(len(queries)):
            value = dp[queries[i][1]+1]-dp[queries[i][0]]
            ans.append(value)
        return ans
        
