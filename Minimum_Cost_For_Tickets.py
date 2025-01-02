class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]*365
        day = [-1]*365
        for i in days:
            day[i-1] = 1

        for i in range(365):
            if day[i] == -1:
                if i == 0:
                    continue
                dp[i] = dp[i-1]
            else:
                option_1 = dp[i-1] + costs[0]
                option_2 = dp[i-7] + costs[1] if i-7 >= 0 else costs[1]
                option_3 = dp[i-30] + costs[2] if i-30 >= 0 else costs[2]
                dp[i] = min(option_1, option_2, option_3)
        return dp[364]
            
