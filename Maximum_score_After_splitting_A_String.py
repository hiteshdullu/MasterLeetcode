class Solution:
    def maxScore(self, s: str) -> int:
        one_count = s.count("1")
        zero_count = 0
        left_one = 0
        max_ans = 0
        for i in range(len(s)-1):
            if s[i] == "0":
                zero_count +=1
            else:
                left_one +=1
            ans = zero_count + one_count - left_one
            max_ans = max(max_ans, ans)
        return max_ans
