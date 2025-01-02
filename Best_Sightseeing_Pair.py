class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_pre = [values[0], 0]
        max_pre_sum = sum(max_pre)
        max_ans = 0
        for i in range(1, len(values)):
            ans = max_pre_sum + values[i] - i
            max_ans = max(max_ans, ans)
            max_pre_sum = max(max_pre_sum, values[i] + i)
        return max_ans
